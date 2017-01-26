# strangle
Alows easy python usage of strings.
```python
from strangle import strangle
x = 1
y = 2.0
plus_result = "3.0"
print strangle("{x}+{y}={plus_result}")  # Prints: 1+2.0=3.0
```

Now you don't need to format your strings with %s %r or %d, or even number them by order of appearance.
you can just call them by their name which makes your code so so so much more readable!

instead of ```python
print "Hello, %s :) What a nice %s?" % (username, time_of_day)```
how about ```python
print strangle("Hello {username} :), What a nice {time_of_day}?")```


Althought i gotta say the name strangle is pretty stupid, I didn't put much effort into this name. 
so hit me up with better ideas and i'll post your name here :) 
