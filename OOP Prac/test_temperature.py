from Temperature import *
import unittest


class TestTemperature(unittest.TestCase):
    
    def testGetCelsius(self):
        degree = Temperature(27)
        self.assertEqual(degree.getCelsius(), 27)

    def testZero(self):
        degree = Temperature(0)
        self.assertEqual(degree.getFahrenheit(), 32)

    def testHundred(self):
        degree = Temperature(100)
        self.assertEqual(degree.getFahrenheit(), 212)
    
    def testTypeError(self):
        with self.assertRaises(TypeError):
            degree = Temperature(True)
        with self.assertRaises(TypeError):
            degree = Temperature("100")
        

unittest.main()
