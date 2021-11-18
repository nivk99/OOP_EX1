import unittest

from callForElevator import CallForElevator
from elevator import Elevator
from building import Building
from offlineAlgo import OfflineAlgo


class MyTestCase(unittest.TestCase):
    """
    It is a class of test which tests the algorithm.
    It creates calls, elevators and a new building and
    performs the test for which call the elevator is suitable for
    """
    def test_OfflineAlgo(self):
        call = []
        c1 = CallForElevator(name="c1", time=10.5, src=-5, dest=10, flag=0, id_elev=-1)
        call.append(c1)
        c2 = CallForElevator(name="c2", time=20.87, src=-10, dest=100, flag=0, id_elev=-1)
        call.append(c2)
        c3 = CallForElevator(name="c3", time=20.88, src=-1, dest=19, flag=0, id_elev=-1)
        call.append(c3)
        c4 = CallForElevator(name="c4", time=30.5, src=0, dest=30, flag=0, id_elev=-1)
        call.append(c4)
        c5 = CallForElevator(name="c5", time=31.5, src=30, dest=-5, flag=0, id_elev=-1)
        call.append(c5)
        c6 = CallForElevator(name="c6", time=32, src=100, dest=-10, flag=0, id_elev=-1)
        call.append(c6)
        c7 = CallForElevator(name="c7", time=80, src=5, dest=10, flag=0, id_elev=-1)
        call.append(c7)
        c8 = CallForElevator(name="c8", time=80, src=-9, dest=10, flag=0, id_elev=-1)
        call.append(c8)
        c9 = CallForElevator(name="c9", time=150, src=50, dest=-10, flag=0, id_elev=-1)
        call.append(c9)
        c10 = CallForElevator(name="c10", time=250, src=0, dest=1, flag=0, id_elev=-1)
        call.append(c10)
        elev = [Elevator(_id=0, _speed=1.5, _minFloor=-10, _maxFloor=100, _closeTime=1.3, _openTime=1.5, _startTime=2.2,
                         _stopTime=3.3),
                Elevator(_id=1, _speed=3, _minFloor=-10, _maxFloor=100, _closeTime=3, _openTime=1.5, _startTime=2.2,
                         _stopTime=3.3),
                Elevator(_id=2, _speed=5, _minFloor=-10, _maxFloor=100, _closeTime=2.5, _openTime=1.5, _startTime=1.5,
                         _stopTime=3.3),
                Elevator(_id=3, _speed=0.5, _minFloor=-10, _maxFloor=100, _closeTime=20, _openTime=25, _startTime=34,
                         _stopTime=3.3)]
        bild = Building(_BuildingName="bild", _minFloor=-10, _maxFloor=100, _listElev=elev)

        OfflineAlgo(building=bild, call=call)

        self.assertEqual(c1.getIdElev(), 2)  # The fastest elevator (2)
        self.assertEqual(c2.getIdElev(), 2)  # The fastest elevator (2)
        self.assertEqual(c3.getIdElev(), 1)  # The fast elevator is occupied so the second good elevator is 1
        self.assertEqual(c4.getIdElev(), 0)  # The fast elevator is occupied so the second good elevator is 1
        self.assertEqual(c5.getIdElev(), 1)  # Elevator 1 and also 2 are occupied so 0 is the fastest to reach the
        # destination
        self.assertEqual(c6.getIdElev(), 2)  # Elevator 2 is / on the way to the 100th floor so it is the best
        self.assertEqual(c7.getIdElev(), 1)  # Elevator 3 is really slow so it is recommended not to take it.
        # Therefore the available elevator is 1
        self.assertEqual(c8.getIdElev(), 0)  # Elevator 0 is finished so it is the best
        self.assertEqual(c9.getIdElev(), 2)  # Elevator 2 is finished so it is the best
        """
        Because elevator 0 is at 10
        Elevator 1 is at 10
         Elevator 2 is at 10 -
         And 3 slow elevator
          Therefore we chose the elevator 2 to the 0th floor because it is the fastest and
           finished all the calls to the floors
        """
        self.assertEqual(c10.getIdElev(), 2)


if __name__ == '__main__':
    unittest.main()
