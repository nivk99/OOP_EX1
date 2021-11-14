import json
import csv
import math

from building import Building
from elevator import Elevator
from callForElevator import CallForElevator
from offlineAlgo import OfflineAlgo


class WritingReading:

    def __init__(self, file_name_json: str = None, file_name_cvs: str = None, output: str = None) -> None:
        self._file_name_cvs = file_name_cvs
        self._file_name_json = file_name_json
        self._file_name_output = output
        self._calls = []
        self._building = Building()
        self.Run()

    def Run(self) -> None:
        self.readingCsv()
        self.readingJson()
        self.algo()
        self.writingCsv()

    def algo(self) -> None:
        OfflineAlgo(building=self._building, call=self._calls)

    def writingCsv(self):
        new_call = []
        for call in self._calls:
            new_call.append(call.__dict__.values())
        with open(self._file_name_output, 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerows(new_call)

    def readingCsv(self) -> None:
        with open(self._file_name_cvs, "r") as file:
            read = csv.reader(file)
            for row in read:
                call = CallForElevator(name=row[0], time=float(row[1]), src=int(row[2]), dest=int(row[3]),
                                       flag=int(row[4]), id_elev=int(row[5]))
                self._calls.append(call)

    def readingJson(self) -> None:
        self._building._BuildingName = self._file_name_json
        arr = []
        with open(self._file_name_json, "r") as f:
            dict_arr = json.load(f)
            self._building._minFloor = dict_arr["_minFloor"]
            self._building._maxFloor = dict_arr["_maxFloor"]
            for v in dict_arr["_elevators"]:
                e = Elevator(**v)
                arr.append(e)
            self._building._listElev = arr


if __name__ == '__main__':
    m = WritingReading("Ex1_Buildings/B2.json", "Ex1_Calls/Calls_a.csv", "o.csv")
