import unittest
import sphere
import math

class TestSphereVolume(unittest.TestCase):

    def test_volume_1(self):
        self.assertAlmostEqual(sphere.volume(1), (4/3)*math.pi*(1**3))

    def test_volume_5(self):
        self.assertAlmostEqual(sphere.volume(5), (4/3)*math.pi*(125))

    def test_volume_10(self):
        self.assertAlmostEqual(sphere.volume(10), (4/3)*math.pi*(1000))

if __name__ == "__main__":
    unittest.main()
