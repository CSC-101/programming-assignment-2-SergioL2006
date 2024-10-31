import data
from data import Point
from data import Rectangle
from data import Duration
from data import Song
# Write your functions for each part in the space below.

# Part 1
#Inputs two points and obtains the rectangle
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
#Puts in a list of songs and the length of what is needed of the song
def songs_shorter_than(list:list[Song], dur:Duration) -> list[Song]:
    within_time = []
    #holds the songs that fall under time
    for x in list:
        if  x.duration.minutes * 60 + x.duration.seconds < dur.minutes * 60 + dur.seconds:
            within_time.append(x)
    #Checks if all together converting minutes to seconds if the duration falls under the wanted time
    return within_time

# Part 4
#Inputs a song list and then depending on where in the order or playlist it is, it will get played
def running_time(songs:list[Song], order:list[int]) -> Duration:
    totalTime = Duration(0,0)
    #Begins by going through the order and using x as the indx for what songs time to add on
    for x in order:
        if x >= 0 and x < len(songs):
            totalTime.seconds += songs[x].duration.seconds
            totalTime.minutes += songs[x].duration.minutes
    #Conversion if seconds is over 60 to minutes
    while totalTime.seconds > 60:
        totalTime.seconds = totalTime.seconds - 60
        totalTime.minutes += 1

    return totalTime


# Part 5
#Checks if the route being taken is valide or not
def validate_route(cityLinks:list[list[str]], route:list[str]) -> bool:
    check = 0
    #Check value then x that goes through the inbedded list
    for x in cityLinks:
        j = 0
        #j used to go through the route and check if it matches with the connected locations (x)
        while j < (len(route)-1):
            if (route[j] == x[0] or route[j+1] == x[0]) and (route[j] == x[1] or route[j+1] == x[1]):
                check += 1
            j += 1

    #If it was correct then the marker should be 1 less then total length of the route's list
    if check == (len(route)-1):
        return True
    else:
        return False

# Part 6
#Checks for longest repeating integers in list, returning None if they do not repeat
def longest_repetion(rep:list[int]):
    #tempary list, longest as final list, and j as a value to sort check if the values repeat
    j = 0
    longest = []
    temp = []
    for x in rep:
        #appends if the list repeats with value of x
        while j < (len(rep)-1):
            if rep[j] == x:
                temp.append(rep[j])
            j += 1
        #if thers a longer list added to temp then it changes longest to temp then temp resets to check next values as well a j as it begins at 0 or beginning of the list
        if len(longest) < len(temp):
            longest = temp
        temp = []
        j = 0
    #Checks if it repeats which it would if longest has a length more than 1
    if len(longest) == 1:
        return None

    return longest
