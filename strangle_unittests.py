from unittest import TestCase

from strangle import strangle


class StrangleTest(TestCase):
    def test_basic_string(self):
        s = strangle("Hello")

        self.assertEqual(str(s), "Hello")

    def test_single_strangle_indicator(self):
        world = "World!"
        s = strangle("Hello {world}")

        self.assertEqual(str(s), "Hello World!")

    def test_multi_strangle_indicator(self):
        x = 6
        y = 7
        expected_str = "6+7=13"
        actual_str = str(strangle("{x}+7=13"))

        self.assertEqual(expected_str, actual_str)