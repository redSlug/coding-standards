"""Module for printing PEP8 recommendations
"""


def print_pep_8_recommendation():
    """
    A magical function, prints important info.
    :return:
    """
    print("public modules, functions, classes, & methods need docstrings.")


class ExampleClass:
    """
    Don't forget to add your docstrings to classes!
    """

    def __init__(self, x):
        self._x = x

    def print_pep_8_guideline(self):
        """
        Prints important guideline
        :return:
        """
        print("don't forget your docstrings in your PUBLIC methods!")
        return self._x + 1


class ParentClass:
    __no_child_conflict = None
    _privateish_to_child = None


print([name for name in dir(ParentClass) if "child" in name])

# ['_ParentClass__no_child_conflict', '_privateish_to_child']


def handle_value(s):
    pass


def key_not_found(s):
    pass


def dummy_function_wrong(key):
    try:
        # Too broad!
        return handle_value(collection[key])
    except KeyError:
        # Will also catch KeyError raised by handle_value()
        return key_not_found(key)


def dummy_function_right(key):
    try:
        value = collection[key]
    except KeyError:
        return key_not_found(key)
    else:
        handle_value(value)


def foo(x):
    if x >= 0:
        return math.sqrt(x)


def bar(x):
    if x < 0:
        return
    return math.sqrt(x)


def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None


def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)


if type(obj) is type(1):
    pass


if isinstance(obj, int):
    pass


seq = ""

if len(seq):
    pass

if not len(seq):
    pass

if not seq:
    pass

if seq:
    pass

# statsd.increment("fun_class.sender", tags=["status:success"])
#
# statsd.increment("silly_class.sender", tags=["result:success"])

statsd.increment("fun_class.sender", tags=["status:success"])

statsd.increment("silly_class.sender", tags=["status:success"])
