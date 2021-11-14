import math

from building import Building
from callForElevator import CallForElevator
from elevator import Elevator


def ExecutionTime(call: CallForElevator, elev: Elevator) -> (bool, float):
    total_floors = math.fabs(call.getDest() - call.getSrc())
    if elev.getCall() is not None:
        if elev.getCall().getTime() == call.getTime() and elev.getCall().getSrc() == call.getSrc() and elev.getState() == call.getStatus():
            if (elev.getCall().getDest() < call.getDest() and elev.getState() == 1) or elev.getCall().getDest()>call.getDest() and elev.getState()==-1:
                t1 = total_floors / elev.getSpeed()
                t2 = 3*(elev.getCloseTime() + elev.getOpenTime() + elev.getStartTime() + elev.getStopTime())
                elev.setWorkTime(t1+t2)
                elev.setCall(cl=call)
            call.setIdElev(id_elev=elev._id)
            return False, 0

    if elev.getType() == call.getSrc() and elev.getFinishTime() > call.getTime():
        t0=elev.getFinishTime() - call.getTime()
        t1 = total_floors / elev.getSpeed()
        t2 = 2 * elev.getCloseTime() + elev.getOpenTime() + elev.getStartTime() + elev.getStopTime()

        return True, t0+t1+t2
    if elev.getFinishTime() < call.getTime():
        if elev.getType() == call.getSrc():
            t1 = total_floors / elev.getSpeed()
            t2 = 2 * elev.getCloseTime() + elev.getOpenTime() + elev.getStartTime() + elev.getStopTime()
            elev.setCall(cl=call)
            elev.setWorkTime(work=t1 + t2)
            call.setIdElev(id_elev=elev._id)
            return False, 0
        total_floors = total_floors + math.fabs(elev.getType() - call.getSrc())
        t1 = total_floors / elev.getSpeed()
        t2 = 2 * (elev.getCloseTime() + elev.getOpenTime() + elev.getStartTime() + elev.getStopTime())
        return True, t1 + t2
    if (call.getStatus() == elev.getState() == 1 and elev.getType() < call.getSrc()) or (
            call.getStatus() == elev.getState() == -1 and elev.getType() > call.getSrc()):
        total_time = elev.getFinishTime() - call.getTime()
        total_floors = total_floors + math.fabs(elev.getType() - call.getSrc())
        t1 = total_floors / elev.getSpeed()
        t2 = 2 * (elev.getCloseTime() + elev.getOpenTime() + elev.getStartTime() + elev.getStopTime())
        return True, total_time + t1 + t2
    if elev.getCall().getDest() > call.getDest() > call.getSrc() > elev.getCall().getSrc() or elev.getCall().getDest() < call.getDest() < call.getSrc() < elev.getCall().getSrc():
        t1 = elev.getFinishTime() - call.getTime()
        t2 = 2 * (elev.getCloseTime() + elev.getOpenTime() + elev.getStartTime() + elev.getStopTime())
        elev.setWorkTime(work=t1 + t2)
        call.setIdElev(id_elev=elev._id)
        return False, 0
    t1 = elev.getFinishTime() - call.getTime()
    t2 = 2 * (elev.getCloseTime() + elev.getOpenTime() + elev.getStartTime() + elev.getStopTime())
    t3 = math.fabs(call.getDest() - elev.getType())/elev.getSpeed()
    return True, t1+t2+t3


class OfflineAlgo:
    def __init__(self, building: Building = None, call: list = None) -> None:
        self._building = building
        self._call = call
        self._list_elevator = self._building.getListElev()
        self.allocateAnElevator()
        print(self._list_elevator)

    def allocateAnElevator(self) -> None:
        for call in self._call:
            new_list = {}
            bo = True
            for elev in self._list_elevator:
                elev.setTimeNow(now=call.getTime())
                ans = ExecutionTime(call=call, elev=elev)
                if ans[0] is False:
                    bo=False
                    break
                else:
                    new_list.update({elev._id: ans[1]})

            total = 500
            Id = 0
            for i in new_list:
                if new_list.get(i) < total:
                    total = new_list.get(i)
                    Id = i
            if bo:
                call.setIdElev(id_elev=Id)
                self._list_elevator[Id].setWorkTime(work=total)
                self._list_elevator[Id].setCall(cl=call)

