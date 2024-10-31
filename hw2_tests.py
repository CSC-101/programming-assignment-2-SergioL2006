import data
import hw2
import unittest
from data import Point
from data import Rectangle
from data import Duration
from data import Song

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_part1_1(self):
        point1 = Point(2,2)
        point2 = Point(10,10)
        result = hw2.create_a_rectangle(point1, point2)
        check = Rectangle(Point(2,10), Point(10,2))
        self.assertEqual(check, result)

    def test_part1_2(self):
        point1 = Point(5,12)
        point2 = Point(24,1)
        result = hw2.create_a_rectangle(point1, point2)
        check = Rectangle(Point(5,12), Point(24,1))
        self.assertEqual(check, result)

    # Part 2
    def test_part2_1(self):
        d1 = Duration(23,12)
        d2 = Duration(23,4)
        result = hw2.shorter_duration_than(d1, d2)
        check = False
        self.assertEqual(check, result)

    def test_part2_2(self):
        d1 = Duration(12,32)
        d2 = Duration(53,17)
        result = hw2.shorter_duration_than(d1, d2)
        check = True
        self.assertEqual(check, result)

    # Part 3
    def test_part3_1(self):
        songList = [Song("Tyler", "song1", Duration(3,21)),Song("SZA", "song2", Duration(2,12)), Song("Kendrick", "song3", Duration(1,23))]
        result = hw2.songs_shorter_than(songList, Duration(2,30))
        check = [Song("SZA", "song2", Duration(2,12)), Song("Kendrick","song3",Duration(1,23))]
        self.assertEqual(check, result)

    def test_part3_2(self):
        songList = [Song("Charlie", "song1", Duration(0,45)),Song("Dre", "song2", Duration(5,6)), Song("Rizzler", "song3", Duration(1,27))]
        result = hw2.songs_shorter_than(songList, Duration(1,45))
        check = [Song("Charlie", "song1", Duration(0,45)), Song("Rizzler","song3",Duration(1,27))]
        self.assertEqual(check, result)

    # Part 4
    def test_part4_1(self):
        songList = [Song("Tyler", "song1", Duration(3, 21)), Song("SZA", "song2", Duration(2, 12)),Song("Kendrick", "song3", Duration(1, 23))]
        playlist = [0,2,0,1]
        result = hw2.running_time(songList, playlist)
        check = Duration(10,17)
        self.assertEqual(check, result)

    def test_part4_2(self):
        songList = [Song("Tyler", "song1", Duration(3, 21)), Song("SZA", "song2", Duration(2, 12)),Song("Kendrick", "song3", Duration(1, 23))]
        playlist = [0,-1,0,1,2,2,4]
        result = hw2.running_time(songList, playlist)
        check = Duration(11,40)
        self.assertEqual(check, result)


    # Part 5
    def test_part5_1(self):
        city_links = [['san luis obispo', 'santa margarita'],['san luis obispo', 'pismo beach'],['atascadero', 'santa margarita'],['atascadero', 'creston']]
        route = ['san luis obispo', 'santa margarita']
        result = hw2.validate_route(city_links, route)
        check = True
        self.assertEqual(check, result)

    def test_part5_2(self):
        city_links = [['san luis obispo', 'santa margarita'],['san luis obispo', 'pismo beach'],['atascadero', 'santa margarita'],['atascadero', 'creston']]
        route = ['santa margarita', 'san luis obispo']
        result = hw2.validate_route(city_links, route)
        check = True
        self.assertEqual(check, result)

    def test_part5_3(self):
        city_links = [['san luis obispo', 'santa margarita'],['san luis obispo', 'pismo beach'],['atascadero', 'santa margarita'],['atascadero', 'creston']]
        route = ['santa margarita', 'san luis obispo', 'pismo beach']
        result = hw2.validate_route(city_links, route)
        check = True
        self.assertEqual(check, result)

    # Part 6
    def test_part6_1(self):
        nums = [1,1,2,2,2,3]
        result = hw2.longest_repetion(nums)
        check = [2,2,2]
        self.assertEqual(check, result)




if __name__ == '__main__':
    unittest.main()
