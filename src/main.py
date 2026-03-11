import argparse

from tabulate import tabulate

from loader import load_data
from reports import REPORTS


def args_parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--report", required=True, choices=REPORTS.keys())
    return parser.parse_args()


def main():
    args = args_parse()

    print("Файлы для загрузки:", args.files)
    data = load_data(args.files)
    print("Загруженные данные:", data)
    report = REPORTS[args.report]()
    result = report.build(data)

    print(tabulate(result, headers="keys", tablefmt="github"))


if __name__ == "__main__":
    main()
