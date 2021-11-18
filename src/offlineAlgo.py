import sys
from typing import List
from building import Building
from callForElevator import CallForElevator
from elevator import Elevator


class OfflineAlgo:
    """
This is an algorithm department for embedding an elevator call.
The algorithm initially checks whether the readings are not in the appropriate range.
It then checks to see if there are calls from the same place and time. If so it goes into a common list.
In addition she checks which elevator takes her to do the task in the shortest time possible.
    """

    def __init__(self, building: Building = None, call: List[CallForElevator] = None) -> None:
        """
        It is a function which builds the algorithm class
        :param building:The building with the elevators
        :param call:All call
        """
        self._building = building
        self._call = call
        self._list_elevator = self._building.getListElev()
        self.allocateAnElevator()

    def allocateAnElevator(self) -> None:
        """
         It is a function that goes through all the elevators and calls and finds the elevator in the most minimal time on time and by the location of the elevator.
         Finally go through the array of the same reading if there are readings at the same time and place
        :return: None
        """
        for call in self._call:
            if call.getSrc() < self._building.getMinFloor() or call.getSrc() > self._building.getMaxFloor() or call.getDest() > self._building.getMaxFloor() or call.getDest() < self._building.getMinFloor():
                raise Exception("out of range")
            min_time = sys.maxsize
            for elev in self._list_elevator:
                way = abs(call.getSrc() - call.getDest())
                way += abs(elev.pos_and_time[0] - call.getSrc())
                _time = way / elev.getSpeed() + 2 * (
                        elev.getStartTime() + elev.getStopTime() + elev.getOpenTime() + elev.getStopTime())
                if elev.pos_and_time[1] >= call.getTime():
                    _time += elev.pos_and_time[1] - call.getTime()
                elif elev.pos_and_time[0] == call.getSrc():
                    _time -= (elev.getStartTime() + elev.getStopTime())
                if min_time > _time:
                    min_time = _time
                    elev_temp = elev
            call.setIdElev(elev_temp.getId())
            elev_temp.pos_and_time[0] = call.getDest()
            elev_temp.pos_and_time[1] = call.getTime() + min_time

