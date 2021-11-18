import unittest

from elevator import Elevator
from building import Building

elev_list = [Elevator(0, 1.5, -1, 10, 1, 1, 2, 2), Elevator(1, 1.5, -1, 10, 2, 2, 3, 3),
             Elevator(2, 1.5, -1, 10, 3, 3, 4, 4), Elevator(3, 1.5, -1, 10, 4, 4, 5, 5),
             Elevator(4, 1.5, -1, 10, 5, 5, 6, 6), Elevator(5, 1.5, -1, 10, 6, 6, 7, 7)]
b1 = Building("b", -1, 10, elev_list)
b2 = Building("b", 0, 11, elev_list)
b3 = Building("b", -5, 15, elev_list)


class MyTestCase(unittest.TestCase):

    """
    It's the building's inspection department.
    She creates a building and elevators and tests the functions in the ward
    """

    def test_getMinFloor(self) -> Exception:
        """
        Test function of getMinFloor
        :return:Exception
        """
        self.assertEqual(b1.getMinFloor(), -1)
        self.assertEqual(b2.getMinFloor(), 0)
        self.assertEqual(b3.getMinFloor(), -5)

    def test_getMaxFloor(self) -> Exception:
        """
        Test function of getMaxFloor
        :return: Exception
        """
        self.assertEqual(b1.getMaxFloor(), 10)
        self.assertEqual(b2.getMaxFloor(), 11)
        self.assertEqual(b3.getMaxFloor(), 15)

    def test_getListElev(self) -> Exception:
        """
        Test function of getListElev
        :return:Exception
        """
        self.assertEqual(b1.getListElev(), elev_list)
        self.assertEqual(b2.getListElev(), elev_list)
        self.assertEqual(b3.getListElev(), elev_list)


if __name__ == '__main__':
    unittest.main()
