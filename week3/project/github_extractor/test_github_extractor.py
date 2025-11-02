import os
import json
import csv
import pytest
import requests
from unittest.mock import patch, MagicMock
from main import fetch_repos, save_data

# ---------- TEST 1: SUCCESSFUL API RESPONSE ----------
@patch("main.requests.get")
def test_fetch_repos_success(mock_get):
    """✅ Should return repo data when API call succeeds"""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"name": "test-repo"}]
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    repos = fetch_repos("dummyuser")

    assert isinstance(repos, list)
    assert repos[0]["name"] == "test-repo"
    mock_get.assert_called_once()

# ---------- TEST 2: RETRY LOGIC ----------
@patch("main.requests.get")
def test_fetch_repos_with_retries(mock_get):
    """🔁 Should retry on timeout and eventually succeed"""
    mock_resp_success = MagicMock()
    mock_resp_success.status_code = 200
    mock_resp_success.json.return_value = [{"name": "final-repo"}]
    mock_resp_success.raise_for_status.return_value = None

    mock_get.side_effect = [
        requests.exceptions.Timeout("Timeout"),
        requests.exceptions.ConnectionError("Connection error"),
        mock_resp_success,
    ]

    repos = fetch_repos("dummyuser")
    assert repos[0]["name"] == "final-repo"
    assert mock_get.call_count == 3

# ---------- TEST 3: SAVE DATA ----------
def test_save_data(tmp_path):
    """💾 Should create valid CSV and JSON output files"""
    repos = [
        {
            "name": "repo1",
            "stargazers_count": 10,
            "forks_count": 2,
            "language": "Python",
            "updated_at": "2025-11-02T12:00:00Z",
        }
    ]

    os.makedirs(tmp_path, exist_ok=True)
    os.chdir(tmp_path)  # switch to temp dir

    save_data("dummyuser", repos)

    # Verify files
    files = os.listdir("week3/project/github_extractor/data")
    csv_file = next((f for f in files if f.endswith(".csv")), None)
    json_file = next((f for f in files if f.endswith(".json")), None)

    assert csv_file and json_file

    # Verify content
    with open(f"week3/project/github_extractor/data/{csv_file}") as f:
        reader = list(csv.DictReader(f))
        assert reader[0]["name"] == "repo1"

    with open(f"week3/project/github_extractor/data/{json_file}") as f:
        data = json.load(f)
        assert data[0]["language"] == "Python"
