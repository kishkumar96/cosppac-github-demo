import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from forecast_summary import summarize_forecast


def test_summarize_forecast_valid_reading():
    forecast = {"station": "auasi", "wave_height_m": 1.8}
    result = summarize_forecast(forecast)
    assert result["station"] == "auasi"
    assert result["wave_height_m"] == 1.8


def test_summarize_forecast_includes_station_in_summary():
    forecast = {"station": "auasi", "wave_height_m": 1.8}
    result = summarize_forecast(forecast)
    assert "auasi" in result["summary"]


def test_summarize_forecast_includes_timestamp_in_summary():
    forecast = {"station": "auasi", "wave_height_m": 1.8, "timestamp": "2026-08-26T06:00:00Z"}
    result = summarize_forecast(forecast)
    assert result["timestamp"] == "2026-08-26T06:00:00Z"
    assert "2026-08-26T06:00:00Z" in result["summary"]
