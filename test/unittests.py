from unittest import TestCase

from fstring import fstring


class FstringTest(TestCase):
    def test_basic_string(self):
        s = fstring("Hello")

        self.assertEqual(str(s), "Hello")

    def test_single_fstring_indicator(self):
        world = "World!"
        s = fstring("Hello {world}")

        self.assertEqual(str(s), "Hello World!")

    def test_multi_fstring_indicator(self):
        x = 6
        y = 7
        result = 13
        expected_str = "6+7=13"
        actual_str = str(fstring("{x}+{y}={result}"))

        self.assertEqual(expected_str, actual_str)

    def test_dictionary_fstring(self):
        simple_dict = {'x': '5', 'y': '10'}
        expected_str = "5!=10"
        actual_str = str(fstring("{simple_dict['x']}!={simple_dict['y']}"))

        self.assertEqual(expected_str, actual_str)

    def test_class_attribute_fstring(self):
        test_object = type('TestObject', (object,), {})
        foo = test_object()
        setattr(foo, 'test', 5)
        expected_str = "foo.test=5"
        actual_str = str(fstring("foo.test={foo.test}"))

        self.assertEqual(expected_str, actual_str)

    def test_math_expr(self):
        expected_str = "4"
        actual_str = str(fstring("{2+2}"))

        self.assertEqual(expected_str, actual_str)

    def test_bool_expr(self):
        x = 5
        y = 5
        expected_str = str(True)
        actual_str = str(fstring("{x==y}"))
        self.assertEqual(expected_str, actual_str)

    def test_equality(self):
        self.assertEqual(fstring("{2+2}"), "4")

    def test_iteration(self):
        expected = ["6", "1"]
        actual = list(fstring("{60+1}"))
        self.assertEqual(actual, expected)

    def test_in(self):
        self.assertIn("6", fstring("{66+1}"))

    def test_formatting(self):
        expected = "a = 4"
        actual = fstring("a = %d")  % 4
        self.assertEqual(expected, actual)

    def test_sort(self):
        arr = [fstring("a"), fstring("b"), fstring('a')]
        actual = sorted(arr)
        expected = [fstring("a"), fstring('a'), fstring("b")]
        self.assertEqual(actual, expected)

    def test_get_item(self):
        self.assertEqual(fstring("44")[0], "4")

    def test_len(self):
        self.assertEqual(len(fstring("44")), 2)

    def test_add_two_fstrings_together(self):
        self.assertEqual(fstring("a") + fstring("b"), "ab")

    def test_add_fstring_and_string(self):
        self.assertEqual(fstring("a") + "b", "ab")

    def add_string_and_fstring(self):
        self.assertEqual("a" + fstring("b"), "ab")

    def test_capitalize(self):
        self.assertEqual(fstring("ab").capitalize(), "Ab")

    def test_repr(self):
        self.assertEqual(repr(fstring("{1}")), "1")