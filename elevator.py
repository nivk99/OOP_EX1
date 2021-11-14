from callForElevator import CallForElevator


class Elevator:
    def __init__(self, _id: int = 0, _speed: float = 0, _minFloor: int = 0, _maxFloor: int = 0, _closeTime: int = 0,
                 _openTime: float = 0, _startTime: float = 0, _stopTime: float = 0, **kwargs) -> None:
        self._id = int(_id)
        self._speed = float(_speed)
        self._minFloor = int(_minFloor)
        self._maxFloor = int(_maxFloor)
        self._closeTime = float(_closeTime)
        self._openTime = float(_openTime)
        self._startTime = float(_startTime)
        self._stopTime = float(_stopTime)
        self._type = -1
        self._state = 0
        self._call = None
        self._finish_time = 0
        self._work_time = 0
        self._time_now = 0

    def getId(self) -> int:
        return self._id

    def getSpeed(self) -> int:
        return self._speed

    def getMinFloor(self) -> int:
        return self._minFloor

    def getMaxFloor(self) -> int:
        return self._maxFloor

    def getCloseTime(self) -> float:
        return self._closeTime

    def getOpenTime(self) -> float:
        return self._openTime

    def getStartTime(self) -> float:
        return self._startTime

    def getStopTime(self) -> float:
        return self._stopTime

    def getState(self) -> int:
        if self._call is not None:
            return self._call.getStatus()
        else:
            return 0

    def getType(self) -> int:
        if self._call is not None:
            return self._call.getDest()
        else:
            return 0

    def getCall(self) -> CallForElevator:
        return self._call

    def getWorkTime(self) -> float:
        return self._work_time

    def getFinishTime(self) -> float:
        if self._call is not None:
            self._finish_time = self._work_time + self._call.getTime()
            return self._finish_time
        return 0

    def getTimeNow(self) -> float:
        return self._time_now

    def setCall(self, cl: CallForElevator) -> None:
        self._call = cl

    def setWorkTime(self, work: float) -> None:
        self._work_time = work

    def setTimeNow(self, now: float) -> None:
        self._time_now = now

    def __str__(self) -> str:
        return f"id:{self._id}, speed:{self._speed}, minFloor:{self._minFloor}, maxFloor:{self._maxFloor}, closeTime:{self._closeTime}, openTime: {self._openTime}, startTime:{self._startTime}, stopTime: {self._stopTime}, finish time: {self._finish_time}"

    def __repr__(self) -> str:
        return f"id:{self._id}, speed:{self._speed}, minFloor:{self._minFloor}, maxFloor:{self._maxFloor}, closeTime:{self._closeTime}, openTime: {self._openTime}, startTime:{self._startTime}, stopTime: {self._stopTime},  finish time: {self._finish_time}"
