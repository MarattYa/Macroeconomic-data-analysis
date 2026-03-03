import csv

def load_data(files):
    if isinstance(files,str):
        files = [files]
    rows = []

    for file in files:
        with open(file,newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                r["gdp"] = float(r["gdp"])
                rows.append(r)
    return rows
