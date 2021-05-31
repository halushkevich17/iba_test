import unittest
import test123


class MyTest123(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
       """class run"""
       print("Run")
       print("++++++++")

    @classmethod
    def tearDownClass(cls):
        """class finish"""
        print("----------")
        print("Finish")


    def setUp(self):
        print("setup for test " + str(self.shortDescription()))

    def tearDown(self):
        print("tearDown for test " + str(self.shortDescription()))


    def test_sum1(self):
        """sum1"""
        self.assertEqual(test123.sum1(2, 4), 36)

    def test_sum2(self):
        """sum2"""
        self.assertNotEqual(test123.sum1(5, 46), 12)

    def test_sum3(self):
        """sum3"""
        self.assertEqual(test123.sum1(-2, -4), 36)

    def test_sum5(self):
        """sum4"""
        self.assertLessEqual(test123.sum1(2, 2), 100)




if __name__ == '__main__':
    unittest.main()
