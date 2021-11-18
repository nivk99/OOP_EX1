

class Elevator:
    """
    It's an elevator class.
     It gets the fields from a file and initializes them
    """

    def __init__(self, _id: int = 0, _speed: float = 0, _minFloor: int = 0, _maxFloor: int = 0, _closeTime: int = 0,
                 _openTime: float = 0, _startTime: float = 0, _stopTime: float = 0, **kwargs) -> None:
        """
        It is a function which builds the elevator department
        :param _id:Elevator number
        :param _speed:Elevator speed to floor
        :param _minFloor: The lowest floor the elevator can reach
        :param _maxFloor:The highest floor the elevator can reach
        :param _closeTime:Door closing time
        :param _openTime: Door opening time
        :param _startTime:Travel start time
        :param _stopTime:Travel stop time
        :param kwargs: All variables
        """
        self._id = int(_id)
        self._speed = float(_speed)
        self._minFloor = int(_minFloor)
        self._maxFloor = int(_maxFloor)
        self._closeTime = float(_closeTime)
        self._openTime = float(_openTime)
        self._startTime = float(_startTime)
        self._stopTime = float(_stopTime)
        self.pos_and_time = [0, 0]

    def __lt__(self, other) -> bool:
        """

        :param other:
        :return:
        """
        return self._speed>other.speed

    def getId(self) -> int:
        """
        the id of this elevator (simple index as in the building)
        :return:Elevator number
        """
        return self._id

    def getSpeed(self) -> float:
        """
        Returns the speed (in floor per second)
        :return:Elevator speed to floor
        """
        return self._speed

    def getMinFloor(self) -> int:
        """
      Returns the minimal floor number to which this Elevator can reach(often a negative value).
      This is the same value as the lowest floor in the building - this elevator belongs to.

        :return:The lowest floor the elevator can reach
        """
        return self._minFloor

    def getMaxFloor(self) -> int:
        """
        Returns the maximal floor number to which this Elevator can reach.
      This is the same value as the highest floor in the building - this elevator belongs to

        :return:The highest floor the elevator can reach
        """
        return self._maxFloor

    def getCloseTime(self) -> float:
        """
        eturns the time (in seconds it takes the Elevator to close its doors
        :return:Door closing time
        """
        return self._closeTime

    def getOpenTime(self) -> float:
        """
        Returns the time (in seconds it takes the Elevator to open its doors
        :return:Door opening time
        """
        return self._openTime

    def getStartTime(self) -> float:
        """
        Return the time in seconds that it takes the elevator to start moving in full speed
        :return:Travel start time
        """
        return self._startTime

    def getStopTime(self) -> float:
        """
        Return the time in seconds that it takes the elevator to stop moving in full speed
        :return:Travel stop time
        """
        return self._stopTime

    def __str__(self) -> str:
        """
         It is a function that returns a string of variables
        :return: A string of variables
        """
        return f"id:{self._id}, speed:{self._speed}, minFloor:{self._minFloor}, maxFloor:{self._maxFloor}, closeTime:{self._closeTime}, openTime: {self._openTime}, startTime:{self._startTime}, stopTime: {self._stopTime}, finish time: {self._finish_time}"

    def __repr__(self) -> str:
        """
       This is a function that returns a list of strings of variables
        :return:List of strings of variables
        """
        return f"id:{self._id}, speed:{self._speed}, minFloor:{self._minFloor}, maxFloor:{self._maxFloor}, closeTime:{self._closeTime}, openTime: {self._openTime}, startTime:{self._startTime}, stopTime: {self._stopTime},  finish time: {self._finish_time}"

