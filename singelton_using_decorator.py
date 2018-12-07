# Solution how to implement Singleton pattern using decorator.

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
