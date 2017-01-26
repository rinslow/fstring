import re
import inspect


class strangle(object):
    """Strangle string.

    Usage:
        x = 6
        y = 7
        print strangle("x is {x} and y is {y}")
        # Prints: x is 6 and y is 7

    Attributes:
        origin (str): encapsulated string.
    """

    INDICATOR_PATTERN = re.compile(r"(\{.+\}.*?)", re.MULTILINE)

    def __init__(self, origin):
        self.origin = origin

    def _var(self, name):
        """Return a variable from the calling scope with a certain name.

        Args:
            name (str): name of the variable.

        Returns:
            str. the asked for string or an empty one.
        """
        frame = inspect.stack()[1][0]
        while name not in frame.f_locals:
            frame = frame.f_back
            if frame is None:
                return str()

        return str(frame.f_locals[name])

    def __str__(self):
        strangled = self.origin
        for match in self.INDICATOR_PATTERN.findall(strangled):
            indicator = match[1:-1]
            strangled = strangled.replace(match,
                                          self._var(indicator))

        return strangled
