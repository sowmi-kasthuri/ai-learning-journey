import os
import pytest
from exchangerate import get_exchange_rate, log_to_csv

def test_get_exchange_rate_returns_float():
    rate = get_exchange_rate("USD", "INR")
    assert isinstance(rate, (float, int)), "Exchange rate should be a number"
    assert rate > 0, "Exchange rate should be positive"

def test_log_to_csv_creates_file(tmp_path):
    log_file = tmp_path / "test_log.csv"
    log_to_csv("USD", "INR", 88.77, filename=log_file)
    assert log_file.exists(), "CSV log file should be created"
    contents = log_file.read_text()
    assert "USD" in contents and "INR" in contents, "Log should contain currency codes"
