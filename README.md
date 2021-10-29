# Class_Study

디스크립터 - getter, setter



Guido van Rossum11 Sep 2012 - Public

Some patterns for fast Python. Know any others?

Avoid overengineering datastructures. Tuples are better than objects (try namedtuple too though). Prefer simple fields over getter/setter functions.

Built-in datatypes are your friends. Use more numbers, strings, tuples, lists, sets, dicts. Also check out the collections library, esp. deque.

Be suspicious of function/method calls; creating a stack frame is expensive.

Don't write Java (or C++, or Javascript, ...) in Python.

Are you sure it's too slow? Profile before optimizing!

The universal speed-up is rewriting small bits of code in C. Do this only when all else fails.
