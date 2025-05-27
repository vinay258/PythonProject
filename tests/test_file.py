import pytest
import unittest

#unittest we can use setup and teardown method
#setUp() runs before every single test method.
#tearDown() runs after every single test method.

class TestMyprogram(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("i am setup class")
    @classmethod
    def tearDownClass(cls):
        print("iam teardown class")

    def test_m1(self):
        print("iam test method one")
    def test_m2(self):
        print("iam test method two")