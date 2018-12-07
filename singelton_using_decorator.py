# Solution how to implement Singleton pattern using decorator.
# Case 1. Using class as decorator

class dec(object):
    obj_instance = None

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        if not self.obj_instance:
            self.obj_instance = self.func()
        return self.obj_instance


@dec
class A(object):
    pass


a1 = A()
a2 = A()

assert a1 == a2

# Case 2. Using function as decorator

_instance = None


def dec1(func):
    def wrapper(*args, **kwargs):
        global _instance
        if not _instance:
            _instance = func()
        return _instance
    return wrapper


@dec1
class B(object):
    pass


b1 = B()
b2 = B()

assert b1 == b2
