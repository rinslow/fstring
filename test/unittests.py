import decimal
import textwrap
from platform import python_version
from unittest import TestCase, main, skipIf, expectedFailure

from fstring import fstring as f


class FstringTest(TestCase):
    def test_basic_string(self):
        s = f("Hello")

        self.assertEqual(str(s), "Hello")

    def test_single_fstring_indicator(self):
        world = "World!"
        s = f("Hello {world}")

        self.assertEqual(str(s), "Hello World!")

    def test_multi_fstring_indicator(self):
        x = 6
        y = 7
        result = 13
        expected_str = "6+7=13"
        actual_str = str(f("{x}+{y}={result}"))

        self.assertEqual(expected_str, actual_str)

    def test_dictionary_fstring(self):
        simple_dict = {'x': '5', 'y': '10'}
        expected_str = "5!=10"
        actual_str = str(f("{simple_dict['x']}!={simple_dict['y']}"))

        self.assertEqual(expected_str, actual_str)

    def test_class_attribute_fstring(self):
        test_object = type('TestObject', (object,), {})
        foo = test_object()
        setattr(foo, 'test', 5)
        expected_str = "foo.test=5"
        actual_str = str(f("foo.test={foo.test}"))

        self.assertEqual(expected_str, actual_str)

    def test_math_expr(self):
        expected_str = "4"
        actual_str = str(f("{2+2}"))

        self.assertEqual(expected_str, actual_str)

    def test_bool_expr(self):
        x = 5
        y = 5
        expected_str = str(True)
        actual_str = str(f("{x==y}"))
        self.assertEqual(expected_str, actual_str)

    def test_equality(self):
        self.assertEqual(f("{2+2}"), "4")

    def test_iteration(self):
        expected = ["6", "1"]
        actual = list(f("{60+1}"))
        self.assertEqual(actual, expected)

    def test_in(self):
        self.assertIn("6", f("{66+1}"))

    def test_formatting(self):
        expected = "a = 4"
        actual = f("a = %d") % 4
        self.assertEqual(expected, actual)

    def test_sort(self):
        arr = [f("a"), f("b"), f('a')]
        actual = sorted(arr)
        expected = [f("a"), f('a'), f("b")]
        self.assertEqual(actual, expected)

    def test_get_item(self):
        self.assertEqual(f("44")[0], "4")

    def test_len(self):
        self.assertEqual(len(f("44")), 2)

    def test_add_two_fstrings_together(self):
        self.assertEqual(f("a") + f("b"), "ab")

    def test_add_fstring_and_string(self):
        self.assertEqual(f("a") + "b", "ab")

    def test_add_string_and_fstring(self):
        self.assertEqual("b" + f("{1+1}"), "b2")

    def test_capitalize(self):
        self.assertEqual(f("ab").capitalize(), "Ab")

    @skipIf(python_version().startswith("3"), "Python 3 repr() has no 'u'")
    def test_repr_python2(self):
        self.assertEqual(repr(f("{u'1'}")), "u'1'")

    @skipIf(python_version().startswith("2"), "Python 2 repr() has 'u' prefix")
    def test_repr_python3(self):
        assert repr(f("{'1'}")) == "'1'"

    @skipIf(python_version().startswith("3"), reason="No unicode in Python 3")
    def test_fstring_returns_unicode_strings(self):
        assert isinstance(f("{1}"), unicode)

    def test_fstring_is_not_bytes(self):
        assert not isinstance(f("{1}"), bytes)

    def test_fstring_as_key_in_a_dict(self):
        dictionary = {f("a"): 4}
        assert f("a") in dictionary
        assert "a" in dictionary
        assert dictionary[f("a")] == 4


class DoubleBracesCase(TestCase):
    def test_double_braces_are_not_tokenized(self):
        assert f("{{}}") == "{}"

    def test_tokens_within_double_braces_are_tokenized(self):
        assert f("{{{4*10}}}") == u"{40}"

    def test_tokens_near_double_braces_are_tokenized_as_well(self):
        assert f("{{{4*10}}}{4}") == "{40}4"

@expectedFailure
class TypeConversionCase(TestCase):
    def test_bad_type_conversion(self):
        with self.assertRaises(SyntaxError):
            f("{6+6}!")

        with self.assertRaises(SyntaxError):
            f("{6+6}!k")

        with self.assertRaises(SyntaxError):
            f("{6+6}!ss")

    def test_ascii_type_conversion(self):
        assert f("{chr(666)!a}") == "'\\u029a'"

    def test_repr_type_conversion(self):
        class Stub:
            def __repr__(self):
                return "Stub"

        assert f("{Stub()!r}") == "Stub"

    def test_str_type_conversion(self):
        class Stub:
            def __str__(self):
                return "Stub"

        assert f("{Stub()!s}") == "Stub"


class UnbalancedBracesCase(TestCase):
    def test_method(self):
        with self.assertRaises(SyntaxError):
            str(f("{{}"))

        # Unbalanced Double braces should not raise a SyntaxError
        try:
            str(f("{{}}}}"))

        except SyntaxError:
            self.fail()

    def test_no_empty_fstring_allowed(self):
        with self.assertRaises(SyntaxError):
            str(f("{}"))


class NewLinesWithinFstringCase(TestCase):
    def test_new_lines(self):
        x = 0
        self.assertEqual(f('''{x
        +1}'''), "1")

        d = {0: 'zero'}
        assert f('''{d[0
]}''') == 'zero'

    def test_newline_strings_are_acceptable(self):
        assert f('''{1+1}
{2+2}''') == '2\n4'

    def test_newline_strings_within_fstring_are_okay(self):
        assert f('''{"""a
b"""}''') == "a\nb"


@expectedFailure
class FormattingCase(TestCase):
    def test_hexadecimal_formatting(self):
        value = 1234
        assert f('input={value:#06x}') == 'input=0x04d2'

    def test_datetime_formatting(self):
        assert f('{date} was on a {date:%A}') == '1991-10-12 was on a Saturday'

    def test_fstrings_in_formatting(self):
        width = 10
        precision = 4
        value = decimal.Decimal('12.34567')
        assert f('{value:{width}.{precision}}') == "12.35"


class EagerEvaluationCase(TestCase):
    def test_fstring_evaluates_eagerly(self):
        a = 4
        b = f("{a}")
        assert b == "4"
        a = 5
        assert b == "4"


if __name__ == '__main__':
    main()
