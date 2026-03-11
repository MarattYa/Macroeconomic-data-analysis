import sys
from pathlib import Path

from main import main


def test_main_runs(monkeypatch):
    test_csv = Path(__file__).resolve().parents[1] / "data" / "economic1.csv"
    test_args = ["main.py", "--files", str(test_csv), "--report", "average-gdp"]
    monkeypatch.setattr(sys, "argv", test_args)

    main()
