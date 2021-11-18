import csv
import unittest

from writingReading import WritingReading


class MyTestCase(unittest.TestCase):
    """
    It classifies tests of reading and writing from a file
    """

    def test_writingReading(self):
        wr = WritingReading("Ex1_Buildings/B5.json", "Ex1_Calls/Calls_d.csv", "out.csv")
        self.assertIsNotNone(wr._building)  # Does the building exist
        ca = wr.getCall()
        for call in ca:  # Is there an inlay that did not exist
            if call.getIdElev == -1:
                self.fail("There can be no negative value after choosing an elevator")

        for elev in wr._building.getListElev():  # Checking for elevators
            if elev is None:
                self.fail("There is a problem with the elevator department code")

        with open("out.csv", "r") as file:  # Checks the result file for existence
            read = csv.reader(file)
            for row in read:
                print("name=" + row[0], "time=" + row[1], "src=" + row[2], "dest=" + row[3],
                      "flag=" + row[4], "id_elev" + row[5])


if __name__ == '__main__':
    unittest.main()
