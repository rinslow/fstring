import re
import inspect


class fstring(object):
    """a formatted string.

    Usage:
        x = 6
        y = 7
        print fstring("x is {x} and y is {y}")
        # Prints: x is 6 and y is 7

    Attributes:
        origin (str): encapsulated string.
    """

    INDICATOR_PATTERN = re.compile(r"(\{.+?\})", re.MULTILINE)

    def __init__(self, origin):
        self.origin = origin

    def _var(self, name):
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

    def __str__(self):
        fstringified = self.origin
        for match in self.INDICATOR_PATTERN.findall(fstringified):
            indicator = match[1:-1]
            parsed_expression = filter(None, re.split(r"(\w+)", indicator))[0]

            frame = self._var(parsed_expression)
            value = eval(indicator, None, frame)
            fstringified = fstringified.replace(match,
                                          str(value))

        return fstringified
