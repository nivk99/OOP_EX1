import math


class CallForElevator:
    def __init__(self, name: str = None, time: float = 0, src: int = 0, dest: int = 0, flag: int = 0, id_elev: int = 0) -> None:
        self._name = name
        self._time = time
        self._src = src
        self._dest = dest
        self._flag = flag
        self._id_elev = id_elev

    def getName(self) -> str:
        return self._name

    def getTime(self) -> float:
        return math.floor(self._time)+1

    def getSrc(self) -> int:
        return self._src

    def getDest(self) -> int:
        return self._dest

    def getFlag(self) -> int:
        return self._flag

    def getIdElev(self) -> int:
        return self._id_elev

    def setFlag(self, flag: int) -> None:
        self._flag = flag

    def setIdElev(self, id_elev) -> None:
        self._id_elev = id_elev

    def getStatus(self) -> int:
        if self._dest > self._src:
            return 1
        else:
            return -1



    def __str__(self) -> str:
        return f"name:{self._name}, time:{self._time}, src:{self._src}, dest:{self._dest}, flag:{self._flag}, Id Elevator:{self._id_elev}"

    def __repr__(self) -> str:
        return f"name:{self._name}, time:{self._time}, src:{self._src}, dest:{self._dest}, flag:{self._flag}, Id Elevator:{self._id_elev}"