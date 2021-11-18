import unittest

from callForElevator import CallForElevator

c1 = CallForElevator("c1", 35, 5, 10, 0, 1)
c2 = CallForElevator("c2", 40, -4, 20, 0, 2)
c3 = CallForElevator("c3", 80, 10, -100, 0, 3)
c4 = CallForElevator("c4", 85, 5, -100, 0, 4)


class MyTestCase(unittest.TestCase):
    """
    It's testing department of elevator calls.
   It creates calls and checks the functions in the class
    """

    def test_getTime(self) -> Exception:
        """
        Test function of getTime
        :return: Exception
        """
        self.assertEqual(c1.getTime(), 35)
        self.assertEqual(c2.getTime(), 40)
        self.assertEqual(c3.getTime(), 80)
        self.assertEqual(c4.getTime(), 85)

    def test_getSrc(self) -> Exception:
        """
        Test function of
        :return: Exception
        """
        self.assertEqual(c1.getSrc(), 5)
        self.assertEqual(c2.getSrc(), -4)
        self.assertEqual(c3.getSrc(), 10)
        self.assertEqual(c4.getSrc(), 5)

    def test_getDest(self) -> Exception:
        """
        Test function of getDest
        :return: Exception
        """
        self.assertEqual(c1.getDest(), 10)
        self.assertEqual(c2.getDest(), 20)
        self.assertEqual(c3.getDest(), -100)
        self.assertEqual(c4.getDest(), -100)

    def test_getIdElev(self) -> Exception:
        """
        Test function of getIdElev
        :return: Exception
        """
        self.assertEqual(c1.getIdElev(), 1)
        self.assertEqual(c2.getIdElev(), 2)
        self.assertEqual(c3.getIdElev(), 3)
        self.assertEqual(c4.getIdElev(), 4)

    def test_getAddListCall(self) -> Exception:
        """
        Test function of getAddListCall
        :return: Exception
        """
        self.assertEqual(c1.getAddListCall(), c1._add_list_call)
        self.assertEqual(c2.getAddListCall(), c2._add_list_call)
        self.assertEqual(c3.getAddListCall(), c3._add_list_call)
        self.assertEqual(c4.getAddListCall(), c4._add_list_call)

    def test_getStatus(self) -> int:
        """
        Test function of getStatus
        :return: int
        """
        self.assertEqual(c1.getStatus(), 1)
        self.assertEqual(c2.getStatus(), 1)
        self.assertEqual(c3.getStatus(), -1)
        self.assertEqual(c4.getStatus(), -1)

    def test_setIdElev(self) -> None:
        """
        Test function of setIdElev
        :return: None
        """
        c1.setIdElev(-1)
        c2.setIdElev(1)
        c3.setIdElev(0)
        c4.setIdElev(2)
        self.assertEqual(c1.getIdElev(), -1)
        self.assertEqual(c2.getIdElev(), 1)
        self.assertEqual(c3.getIdElev(), 0)
        self.assertEqual(c4.getIdElev(), 2)


if __name__ == '__main__':
    unittest.main()
