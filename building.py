from elevator import Elevator
####dsdfsdfsdfsdffff

class Building:
    def __init__(self, _BuildingName: str = None, _minFloor: int = 0, _maxFloor: int = 0, _listElev: list = []) -> None:
        self._BuildingName = _BuildingName
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor
        self._listElev = _listElev

    def getBuildingName(self) -> str:
        return self._BuildingName

    def getMinFloor(self) -> int:
        return self._minFloor

    def getMaxFloor(self) -> int:
        return self._maxFloor

    def getListElev(self) -> list:
        return self._listElev

    def getElevetor(self, id: int) -> Elevator:
        for i in self._listElev:
            if i._id == id:
                return i

    def __str__(self):
        return f"BuildingName:{self._BuildingName}, minFloor:{self._minFloor}, maxFloor:{self._maxFloor}, listElev:{self._listElev}"

    def __repr__(self):
        return f"BuildingName:{self._BuildingName}, minFloor:{self._minFloor}, maxFloor:{self._maxFloor}, listElev:{self._listElev}"
