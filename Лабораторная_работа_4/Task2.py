# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def read_csv(file_path: str, delimiter: str = ","):
    with open(file_path, mode='r', encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)
        data = [row for row in reader]
    return data


def task() -> None:
    ...  # TODO считать содержимое csv файла
    data = read_csv(INPUT_FILENAME, delimiter=",")

    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME, mode='r', encoding='utf-8') as output_f:
        content = output_f.read()
        print(content.rstrip('\n'), end='')

