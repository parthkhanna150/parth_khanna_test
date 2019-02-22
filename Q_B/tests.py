import unittest
from question2 import compare_version

class VersionCompareTests(unittest.TestCase):

    # v1 higher than v2
    def test_higher_1(self):
        result = compare_version('1.2', '1.1')
        self.assertEqual(1,1)

    def test_higher_2(self):
        result = compare_version('4.5.3.2', '4.5')
        self.assertEqual(1,1)

    def test_higher_3(self):
        result = compare_version('-1.5.1', '-1.5.10')
        self.assertEqual(1,1)

    def test_higher_4(self):
        result = compare_version('1.0.1', '1')
        self.assertEqual(1,1)

    # v1 = v2
    def test_equal_1(self):
        result = compare_version('1.3', '1.3')
        self.assertEqual(0,0)

    def test_equal_2(self):
        result = compare_version('1.1', '1.0000001')
        self.assertEqual(0,0)

    # v1 less than v2
    def test_less_1(self):
        result = compare_version('1.1', '1.2')
        self.assertEqual(-1,-1)

    def test_less_2(self):
        result = compare_version('-7.5.10', '-7.5.1')
        self.assertEqual(-1,-1)

    def test_less_3(self):
        result = compare_version('1.1', '1.1.0.1')
        self.assertEqual(-1,-1)


if __name__ == '__main__':
    unittest.main()
