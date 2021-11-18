import sys
from writingReading import WritingReading

"""
Given a csv file and json files, the algorithm will read the files and perform a number of operations:

The algorithm will calculate the location of each elevator in relation to the time of each reading and will be 
entered in another field in the elevator class called pos_and_time.
The algorithm will go through all the requests and place the elevator for each request which will perform its purpose
 in the shortest time of all the elevators (taking into account the given times, the location of the elevator,  the time
 it takes for the elevator to go one floor, the number of elevators, up / down elevator mode and end previous readings.
In some cases the elevator will make several requests simultaneously depending on the situation. As for example the 
elevator goes up from floor x to floor y the elevator will take all requests between x and y (as long as the elevator 
has not passed the source of the additional request).


"""


class Ex1:
    pass


def main():
    """
    This is the main function that starts the algorithm by getting the values
    :return:An answer file for each reading
    """
    json_build, cvs_call, out = sys.argv[1], sys.argv[2], sys.argv[3]
    WritingReading(file_name_json=json_build, file_name_cvs=cvs_call, output=out)


if __name__ == '__main__':
    main()
