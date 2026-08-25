# COSPPac GitHub Demo

A small demo repository built for the **Artificial Intelligence for Coding** session
at the COSPPac Regional ICT Workshop (Melbourne, 27 August 2026).

Nothing here is confidential — this is safe, non-operational sample data,
safe to practise on.

## Structure

```
cosppac-github-demo/
    README.md
    data/
        sample_forecast.json
    scripts/
        forecast_summary.py
    tests/
        test_forecast_summary.py
```

- `scripts/forecast_summary.py` — the script we work on during the demo
- `data/sample_forecast.json` — safe, non-operational sample data
- `tests/test_forecast_summary.py` — checks our work as we go

## Running it

```
pip install pytest
python scripts/forecast_summary.py
pytest tests/
```

## The exact prompts

These are the six prompts used in the live demo. Copy them as-is, or adapt
them to your own script.

1. **Explain**
   > Explain what forecast_summary.py does, especially what happens when wave_height_m is missing.

2. **Find the risks**
   > What could go wrong with this script, especially with missing, negative or non-numeric wave_height_m values?

3. **Add validation**
   > Update forecast_summary.py so a missing wave_height_m value raises a clear validation error, not zero. Do not add new packages.

4. **Add tests**
   > Add pytest tests for forecast_summary.py covering valid, missing, negative and non-numeric wave_height_m values.

5. **Correct it**
   > That default of 0 for a missing reading is wrong — raise an error instead. Regenerate the fix and the tests.

6. **Check the diff**
   > Show me the Git diff of everything you changed, before I commit anything.

## The rule this demo is built around

AI proposes. The developer reviews, tests, and decides.

Every AI suggestion goes through the same steps, every time: read it, test it, diff it, then decide.
