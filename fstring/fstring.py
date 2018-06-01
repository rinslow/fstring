"""PEP 498 Python 2.7 Back-port."""
import re
import inspect
from platform import python_version

from six import text_type
from astroid.decorators import cachedproperty

# pylint: disable=invalid-name,missing-docstring
def python2_cmp(a, b):
    return (a > b) - (a < b)

# pylint: disable=redefined-builtin
if python_version().startswith("3"):
    cmp = python2_cmp

else:
    cmp = cmp


class fstring(text_type):  # pylint: disable=invalid-name
    """a formatted string.

    Usage:
        x = 6
        y = 7
        print fstring("x is {x} and y is {y}")
        # Prints: x is 6 and y is 7

    Attributes:
        origin (text_type): encapsulated string.

    Properties:
        cached_origin (text_type): eagerly evaluated string.
    """

    INDICATOR_PATTERN = re.compile(r"(\{.+?\})", re.MULTILINE | re.UNICODE)

    def __init__(self, origin):
        super(fstring, self).__init__()
        self.origin = text_type(origin)

    @cachedproperty
    def cached_origin(self):
        return self.fstringify()

    @staticmethod
    def get_frame_by_variable_name(name):
        """Return a variable from the calling scope with a certain name.

        Args:
            name (str): name of the variable.

        Returns:
            dict. the locals containing the name or an empty one.
        """
        frame = inspect.stack()[1][0]
        while name not in frame.f_locals:
            frame = frame.f_back
            if frame is None:
                return dict()

        return frame.f_locals

    def fstringify(self):
        fstringified = self.origin
        for match in self.INDICATOR_PATTERN.findall(fstringified):
            indicator = match[1:-1]
            parsed_expression = next(
                iter(filter(None, re.split(r"(\w+)", indicator)))
            )

            frame = self.get_frame_by_variable_name(parsed_expression)
            value = eval(indicator, None, frame)  # pylint: disable=eval-used
            fstringified = fstringified.replace(match, text_type(value))

        return fstringified

    def __str__(self):
        return self.cached_origin

    def __eq__(self, other):
        if type(other) is type(self):
            return self.cached_origin == other.cached_origin

        return self.cached_origin == other

    def __iter__(self):
        return iter(self.cached_origin)

    def __len__(self):
        return len(self.cached_origin)

    def __cmp__(self, other):
        if type(other) is type(self):
            return cmp(self.cached_origin, other.cached_origin)

        return cmp(self.cached_origin, other)

    def __getitem__(self, item):
        return self.cached_origin[item]

    def __mod__(self, other):
        return fstring(self.cached_origin % other)

    def __add__(self, other):
        return fstring(self.cached_origin + text_type(other))

    def __repr__(self):
        return text_type(repr(self.cached_origin))

    def __hash__(self):
        return hash(self.cached_origin)

    def __radd__(self, other):
        return other + self.cached_origin
