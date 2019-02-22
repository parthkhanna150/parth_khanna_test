import unittest
from question1 import are_overlap

class OverlapTests(unittest.TestCase):

    # if input is in regular order i.e. a,b and c,d where a<b AND c<d
    def test_positive_true(self):
        result = are_overlap(3, 5, 1, 9)
        self.assertTrue(result)

    def test_positive_false(self):
        result = are_overlap(3, 7, 8, 9)
        self.assertFalse(result)

    def test_negative_true(self):
        result = are_overlap(-9, -2, -7, -1)
        self.assertTrue(result)

    def test_negative_false(self):
        result = are_overlap(-1, -5, -6, -11)
        self.assertFalse(result)

    def test_pos_neg_true(self):
        result = are_overlap(-3, 1, -7, 0)
        self.assertTrue(result)

    def test_point_true(self):
        result = are_overlap(0, 0, 0, 0)
        self.assertTrue(result)

    def test_line_overlap_true(self):
        result = are_overlap(1, 9, 1, 9)
        self.assertTrue(result)

    def test_pos_neg_false(self):
        result = are_overlap(-3, -2, 2, 4)
        self.assertFalse(result)

    # if input is in inverse order i.e. a,b and c,d where a>b OR c>d
    def test_positive_true_inv(self):
        result = are_overlap(5, 3, 6, 4)
        self.assertTrue(result)

    def test_positive_false_inv(self):
        result = are_overlap(7, 3, 8, 9)
        self.assertFalse(result)

    def test_negative_true_inv(self):
        result = are_overlap(-9, -2, -1, -7)
        self.assertTrue(result)

    def test_negative_false_inv(self):
        result = are_overlap(-5, -1, -11, -6)
        self.assertFalse(result)

    def test_pos_neg_true_inv(self):
        result = are_overlap(-3, 1, 0, -7)
        self.assertTrue(result)

    def test_pos_neg_false_inv(self):
        result = are_overlap(-2, -3, 4, 2)
        self.assertFalse(result)

if __name__ == "__main__":
     unittest.main()
