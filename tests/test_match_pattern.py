from unittest import TestCase

from python_learning.example.match_pattern import *


class Test(TestCase):
    def test_matcher(self):
        matcher([Point(1, 2)])
        self.assertTrue(True, "Debug passed...")
