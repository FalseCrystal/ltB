import unittest
import find_exams

class TestExclude(unittest.TestCase):

      def test_getLect():
           f = open("lectlist.csv")
           testDict = getCoursesforLects(f)

           assertEqual(testDict,[[Levitt,ELEN4010],[Hazelhurst,ElEN7039],[Cronje,ELEN4014],[Dinger,SCMD1003],[Hazelhurst,ELEN3020],[Hazelhurst,COMS7059],[Hofsajer,ELEN3003],[Levitt,ELEN3008],[Hofsajer,ELEN3002]])
           f.close()

if __name__ == '__main__':

     unittest.main() 
