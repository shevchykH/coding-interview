# Solution how to implement Singleton pattern using decorator.
# Case 1. Using class as decorator


class dec(object):
    obj_instance = None

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        if self.obj_instance is None:
            self.obj_instance = self.func(*args, **kwargs)
        return self.obj_instance


@dec
class A(object):
    pass


a1 = A()
a2 = A()

assert id(a1) == id(a2)


# Case 2. Using function as decorator


def dec1(func):
    dec1.instace = None

    def wrapper(*args, **kwargs):
        if hasattr(dec1, "instance"):
            return dec1.instance
        dec1.instance = func(*args, **kwargs)
        return dec1.instance
    return wrapper


@dec1
class B(list):
    pass


b1 = B()
b2 = B()
b2.append(1)

assert id(b1) == id(b2)
