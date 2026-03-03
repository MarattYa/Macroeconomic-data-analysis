from loader import load_data
from pathlib import Path

def test_loader_reads_file():
    test_csv = Path(__file__).resolve().parents[1] / "data" / "economic1.csv"

    rows = load_data([test_csv])

    assert len(rows) > 0
    assert "country" in rows[0]
    assert "gdp" in rows[0]
    assert isinstance(rows[0]["gdp"], float)