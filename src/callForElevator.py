import math


class CallForElevator:
    """
    It's a class of elevator calls.
    It gets the variables from a file and initializes the fields
    """

    def __init__(self, name: str = None, time: float = 0, src: int = 0, dest: int = 0, flag: int = 0,
                 id_elev: int = 0) -> None:
        """
        It is a function that builds the call department of the elevators
        :param name: The name of the call
        :param time:call time
        :param src:Source floor
        :param dest:Target floor
        :param flag: Variable does not matter
        :param id_elev: Elevator number for reading the elevator
        """
        self._name = name
        self._time = time
        self._src = int(src)
        self._dest = int(dest)
        self._flag = int(flag)
        self._id_elev = int(id_elev)

    # def __iter__(self):
    #     return iter([self._name,self._time,self._src,self._dest,self._flag,self._id_elev])

    def getName(self) -> str:
        """
        A function that returns the name of the call
        :return: The name of the call
        """
        return self._name

    def getTime(self) -> float:
        """
        A function that returns the time of a call to an elevator
        :return: call time
        """
        # return math.floor(self._time) + 1
        return self._time

    def getSrc(self) -> int:
        """
        A function that returns the source floor of the call
        :return: Source floor
        """
        return self._src

    def getDest(self) -> int:
        """
        A function that returns the target floor of the call
        :return: Target floor
        """
        return self._dest

    def getIdElev(self) -> int:
        """
        A function that returns the call placement to the elevator
        :return: Elevator number for reading the elevator
        """
        return self._id_elev

    def getAddListCall(self) -> list:
        return self._add_list_call

    def getStatus(self) -> int:
        if self._dest > self._src:
            return 1
        return -1

    def setIdElev(self, id_elev) -> None:
        """
        A function that changes the placement of the call to the elevator
        :param id_elev: Elevator number for reading the elevator
        :return: None
        """
        self._id_elev = id_elev

    def __str__(self) -> str:
        """
         It is a function that returns a string of variables
        :return: A string of variables
        """
        return f"name:{self._name}, time:{self._time}, src:{self._src}, dest:{self._dest}, flag:{self._flag}, Id Elevator:{self._id_elev}"

    def __repr__(self) -> str:
        """
       This is a function that returns a list of strings of variables
        :return:List of strings of variables
        """
        return f"name:{self._name}, time:{self._time}, src:{self._src}, dest:{self._dest}, flag:{self._flag}, Id Elevator:{self._id_elev}"
