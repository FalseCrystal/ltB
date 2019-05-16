import unittest
import find_exams.py

class TestExclude(unittest.TestCase):

      def test_getLect():
           f = open("lectlist.csv")
           testDict = getCoursesforLects(f)

           assertEqual(testDict,f)
           f.close()

if __name__ == '__main__':

unittest.main() 
