from abc import ABC, abstractmethod
import csv


CellValue = str | int | float

class TableReader(ABC):
    @abstractmethod
    def __init__(self, filename: str):
        pass

    @abstractmethod
    def read(self) -> list[list[CellValue]]:
        pass

class CSVReader(TableReader):
    def __init__(self, filename: str):
        self._filename = filename

    def read(self) -> list[list[CellValue]]:
        info_list: list[list[CellValue]] = []
        with open(self._filename, 'r') as fd:
            file_reader = csv.reader(fd, delimiter=',')
            for row in file_reader:
                info_list.append(row)
        print(info_list)
        return info_list

if __name__ == "__main__":
    content = [
        ['Столбец1', 'Столбец2'],
        [0, 1],
        [2, 3],
    ]
    reader = CSVReader('table_csv.csv')
    reader.read()
