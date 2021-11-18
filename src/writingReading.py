import json
import csv
from building import Building
from elevator import Elevator
from callForElevator import CallForElevator
from offlineAlgo import OfflineAlgo


class WritingReading(Elevator, CallForElevator, ):
    """
    It's just a class of writing and reading from a file
    """

    def __init__(self, file_name_json: str = None, file_name_cvs: str = None, output: str = None) -> None:
        """
        It is a function which builds the class.
        :param file_name_json: The building file
        :param file_name_cvs:Elevator call file
        :param output:The file is an answer to elevator calls
        """
        self._file_name_cvs = file_name_cvs
        self._file_name_json = file_name_json
        self._file_name_output = output
        self._calls = []
        self._building = Building()
        self.Run()

    def Run(self) -> None:
        """
        It is a function that runs the functions in the class
        :return: None
        """
        self.readingCsv()
        self.readingJson()
        self.algo()
        self.writingCsv()

    def algo(self) -> None:
        """
        This is a function that calls the algorithm department and checks the best elevator for reading
        :return: None
        """
        OfflineAlgo(building=self._building, call=self._calls)

    def writingCsv(self) -> None:
        """
        It is a function which writes to the file the answer after the answer of the algorithm
        :return:None
        """
        new_call = []
        for call in self._calls:
            new_call.append(call.__dict__.values())
        with open(self._file_name_output, 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerows(new_call)

    def readingCsv(self) -> None:
        """
        This is a function that reads the call file to the elevator and initializes the calls in the class
        :return:None
        """
        with open(self._file_name_cvs, "r") as file:
            read = csv.reader(file)
            for row in read:
                call = CallForElevator(name=row[0], time=float(row[1]), src=int(row[2]), dest=int(row[3]),
                                       flag=int(row[4]), id_elev=int(row[5]))
                self._calls.append(call)

    def readingJson(self) -> None:
        """
        It is a function which absorbs the building and wishes the variables in the department of the elevator and of the building
        :return: None
        """
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

    def getCall(self) -> list:
        return self._calls



