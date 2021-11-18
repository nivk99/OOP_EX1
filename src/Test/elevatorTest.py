import unittest

from elevator import Elevator

e1 = Elevator(0, 1.5, -1, 10, 1, 1.1, 2, 3)
e2 = Elevator(1, 5.5, 5, 11, 2, 2.2, 0, 1)
e3 = Elevator(2, 3.5, 2, 20, 3, 3.3, 8, 3)
e4 = Elevator(3, 2.5, 4, 30, 4, 4.4, 2, 1)
e5 = Elevator(4, 1.5, -5, 50, 5, 5.5, 3, 4)
e6 = Elevator(5, 1, -10, 100, 6, 6.6, 6, 6)


class MyTestCase(unittest.TestCase):
    """"
    It's testing department of the elevators.
    It creates new elevators and tests the functions in its class.
    """
    def test_getId(self) -> Exception:
        """
        Test function of getId
        :return: Exception
        """
        self.assertEqual(e1.getId(), 0)
        self.assertEqual(e2.getId(), 1)
        self.assertEqual(e3.getId(), 2)
        self.assertEqual(e4.getId(), 3)
        self.assertEqual(e5.getId(), 4)
        self.assertEqual(e6.getId(), 5)

    def test_getSpeed(self) -> Exception:
        """
        Test function of getSpeed
        :return: Exception
        """
        self.assertEqual(e1.getSpeed(), 1.5)
        self.assertEqual(e2.getSpeed(), 5.5)
        self.assertEqual(e3.getSpeed(), 3.5)
        self.assertEqual(e4.getSpeed(), 2.5)
        self.assertEqual(e5.getSpeed(), 1.5)
        self.assertEqual(e6.getSpeed(), 1)

    def test_getMinFloor(self) -> Exception:
        """
        Test function of getMinFloor
        :return: Exception
        """
        self.assertEqual(e1.getMinFloor(), -1)
        self.assertEqual(e2.getMinFloor(), 5)
        self.assertEqual(e3.getMinFloor(), 2)
        self.assertEqual(e4.getMinFloor(), 4)
        self.assertEqual(e5.getMinFloor(), -5)
        self.assertEqual(e6.getMinFloor(), -10)

    def test_getMaxFloor(self) -> Exception:
        """
        Test function of getMaxFloor
        :return: Exception
        """
        self.assertEqual(e1.getMaxFloor(), 10)
        self.assertEqual(e2.getMaxFloor(), 11)
        self.assertEqual(e3.getMaxFloor(), 20)
        self.assertEqual(e4.getMaxFloor(), 30)
        self.assertEqual(e5.getMaxFloor(), 50)
        self.assertEqual(e6.getMaxFloor(), 100)

    def test_getCloseTime(self) -> Exception:
        """
        Test function of getCloseTime
        :return: Exception
        """
        self.assertEqual(e1.getCloseTime(), 1)
        self.assertEqual(e2.getCloseTime(), 2)
        self.assertEqual(e3.getCloseTime(), 3)
        self.assertEqual(e4.getCloseTime(), 4)
        self.assertEqual(e5.getCloseTime(), 5)
        self.assertEqual(e6.getCloseTime(), 6)

    def test_getOpenTime(self) -> Exception:
        """
        Test function of getOpenTime
        :return: Exception
        """
        self.assertEqual(e1.getOpenTime(), 1.1)
        self.assertEqual(e2.getOpenTime(), 2.2)
        self.assertEqual(e3.getOpenTime(), 3.3)
        self.assertEqual(e4.getOpenTime(), 4.4)
        self.assertEqual(e5.getOpenTime(), 5.5)
        self.assertEqual(e6.getOpenTime(), 6.6)

    def test_getStartTime(self) -> Exception:
        """
        Test function of getStartTime
        :return: Exception
        """
        self.assertEqual(e1.getStartTime(), 2)
        self.assertEqual(e2.getStartTime(), 0)
        self.assertEqual(e3.getStartTime(), 8)
        self.assertEqual(e4.getStartTime(), 2)
        self.assertEqual(e5.getStartTime(), 3)
        self.assertEqual(e6.getStartTime(), 6)

    def test_getStopTime(self) -> Exception:
        """
        Test function of getStopTime
        :return: Exception
        """
        self.assertEqual(e1.getStopTime(), 3)
        self.assertEqual(e2.getStopTime(), 1)
        self.assertEqual(e3.getStopTime(), 3)
        self.assertEqual(e4.getStopTime(), 1)
        self.assertEqual(e5.getStopTime(), 4)
        self.assertEqual(e6.getStopTime(), 6)


if __name__ == '__main__':
    unittest.main()
