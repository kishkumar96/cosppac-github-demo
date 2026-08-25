"""Summarise a single forecast reading for a monitored station."""

import json
from pathlib import Path


def summarize_forecast(forecast: dict) -> dict:
    station = forecast.get("station", "unknown")
    wave_height = forecast.get("wave_height_m", 0)
    return {
        "station": station,
        "wave_height_m": wave_height,
        "summary": f"Station {station}: wave height {wave_height} m",
    }


if __name__ == "__main__":
    data_path = Path(__file__).resolve().parent.parent / "data" / "sample_forecast.json"
    forecast = json.loads(data_path.read_text())
    result = summarize_forecast(forecast)
    print(result["summary"])
