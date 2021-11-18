from typing import List

from elevator import Elevator


class Building:
    """
    It's a department of the building.
    It gets the variables from a file and initializes them
    """
    def __init__(self, _BuildingName: str = None, _minFloor: int = 0, _maxFloor: int = 0,
                 _listElev: List[Elevator] = []) -> None:
        """
        This is a function that builds the building department

        :param _BuildingName: The name of the building (according to the file name)
        :param _minFloor:The lowest floor in the building
        :param _maxFloor: Highest floor in the building
        :param _listElev:List of all elevators
        """
        self._BuildingName = _BuildingName
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor
        self._listElev = _listElev

    def getBuildingName(self) -> str:
        """
        It is a function that returns the name of the building
        :return: The name of the building
        """
        return self._BuildingName

    def getMinFloor(self) -> int:
        """
        It is a function that returns the lowest floor in the building
        :return: The lowest floor in the building
        """
        return self._minFloor

    def getMaxFloor(self) -> int:
        """
        This is a function that returns the highest floor in the building
        :return: Highest floor in the building
        """
        return self._maxFloor

    def getListElev(self) -> list:
        """
        This is a function that returns the list of elevators
        :return: List of all elevators
        """
        return self._listElev

    def __str__(self) -> str:
        """
        It is a function that returns a string of variables
        :return: A string of variables
        """
        return f"BuildingName:{self._BuildingName}, minFloor:{self._minFloor}, maxFloor:{self._maxFloor}, listElev:{self._listElev}"

    def __repr__(self) -> str:
        """
     This is a function that returns a list of strings of variables
        :return:List of strings of variables
        """
        return f"BuildingName:{self._BuildingName}, minFloor:{self._minFloor}, maxFloor:{self._maxFloor}, listElev:{self._listElev}"
