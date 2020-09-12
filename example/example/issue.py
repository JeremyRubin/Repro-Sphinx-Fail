class A:
    """I am A Class"""
def decorator(b):
    class C:
        t = b
    C.__doc__ = b.__doc__
    return C
@decorator
class B:
    """I am B Class, I am partly Gone"""

import types

def decorator2(name):
    def decorator2_inner(b):
        class C:
            t = b
        C.__doc__ = b.__doc__
        Y = types.new_class(name, bases=(C,))
        Y.__doc__ = Y.__doc__
        return Y
    return decorator2_inner

@decorator2("NEWCLASS")
class D:
    """I am D Class, I am Completely Gone"""
