import pytest
from unittest.mock import patch, MagicMock
import requests
from main import get_weather


@patch("main.requests.get")
def test_get_weather_success(mock_get):
    """✅ Test successful API response"""
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "name": "Chennai",
        "main": {"temp": 30.0, "humidity": 70},
        "weather": [{"description": "sunny"}],
    }
    mock_resp.raise_for_status.return_value = None
    mock_get.return_value = mock_resp

    result = get_weather("Chennai")

    assert result["city"] == "Chennai"
    assert result["temperature"] == 30.0
    assert result["humidity"] == 70
    assert result["description"] == "sunny"


@patch("main.requests.get")
def test_get_weather_not_found(mock_get):
    """❌ Test city not found (404 error)"""
    mock_resp = MagicMock()
    mock_resp.status_code = 404
    mock_resp.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Error")
    mock_get.return_value = mock_resp

    result = get_weather("InvalidCity")
    assert "error" in result
    assert result["error"] == "City not found or bad request"


@patch("main.requests.get")
def test_get_weather_with_retries(mock_get):
    """🔁 Test retry logic: first 2 attempts fail, 3rd succeeds"""
    mock_resp_success = MagicMock()
    mock_resp_success.status_code = 200
    mock_resp_success.json.return_value = {
        "name": "Chennai",
        "main": {"temp": 28.0, "humidity": 55},
        "weather": [{"description": "clear"}],
    }
    mock_resp_success.raise_for_status.return_value = None

    # First two attempts raise errors; third succeeds
    mock_get.side_effect = [
        requests.exceptions.Timeout("Timeout"),
        requests.exceptions.ConnectionError("Connection error"),
        mock_resp_success,
    ]

    result = get_weather("Chennai")

    assert result["city"] == "Chennai"
    assert result["temperature"] == 28.0
    assert result["humidity"] == 55
    assert result["description"] == "clear"
