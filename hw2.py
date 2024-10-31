import data
from data import Point
from data import Rectangle
from data import Duration
from data import Song
# Write your functions for each part in the space below.

# Part 1
def create_a_rectangle(point1: Point, point2: Point) -> Rectangle:
    if point1.x < point2.x:
        pointTopLeftx = point1.xS
        pointBottomRightx = point2.x
    else:
        pointTopLeftx = point2.x
        pointBottomRightx = point1.x
    #Checks where x point should go depending on size of value
    if point1.y > point2.y:
        pointTopLefty = point1.y
        pointBottomRighty = point2.y
    else:
        pointTopLefty = point2.y
        pointBottomRighty = point1.y
    #Checks where y point should go depending on size of value
    pointTopLeft = Point(pointTopLeftx, pointTopLefty)
    pointBottomRight = Point(pointBottomRightx, pointBottomRighty)
    #Creates the points after figuring which other is greater

    return Rectangle(pointTopLeft, pointBottomRight)

# Part 2
def shorter_duration_than(dur1:Duration, dur2:Duration) -> bool:
    totalTimeD1 = dur1.minutes * 60 + dur1.seconds
    totalTimeD2 = dur2.minutes * 60 + dur2.seconds
    #Turns all minutes into seconds then adding all seconds together for comparison
    return totalTimeD1 < totalTimeD2
    #Checks if the first time is less than second time in boolean statement

# Part 3
def songs_shorter_than(list:list[Song], dur:Duration) -> list[Song]:
    within_time = []
    for x in list:
        if  x.duration.minutes * 60 + x.duration.seconds < dur.minutes * 60 + dur.seconds:
            within_time.append(x)

    return within_time

# Part 4
def running_time(songs:list[Song], order:list[int]) -> Duration:
    totalTime = Duration(0,0)

    for x in order:
        if x >= 0 and x < len(songs):
            totalTime.seconds += songs[x].duration.seconds
            totalTime.minutes += songs[x].duration.minutes

    while totalTime.seconds > 60:
        totalTime.seconds = totalTime.seconds - 60
        totalTime.minutes += 1

    return totalTime


# Part 5
def validate_route(cityLinks:list[list[str]], route:list[str]) -> bool:
    check = 0
    for x in cityLinks:
        j = 0
        while j < (len(route)-1):
            if (route[j] == x[0] or route[j+1] == x[0]) and (route[j] == x[1] or route[j+1] == x[1]):
                check += 1
            j += 1


    if check == (len(route)-1):
        return True
    else:
        return False

# Part 6
def longest_repetion(rep:list[int]):
    j = 0
    longest = []
    temp = []
    for x in rep:
        while j < (len(rep)-1):
            if rep[j] == x:
                temp.append(rep[j])
                j += 1
            else:
                if len(longest) < len(temp):
                    longest = temp
                    temp = []
                    j = len(rep)
        j = 0


    return longest
