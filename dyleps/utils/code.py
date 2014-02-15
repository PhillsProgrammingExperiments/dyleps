from functools import wraps
from dyleps.utils.exceptions import AbstractMethodException


def abstract(foo):
    @wraps(foo)
    def decorated(self, *args, **kwargs):
        raise AbstractMethodException("Function %s is abstract!" % foo.__qualname__)
    decorated.abstract =  True
    return decorated

def assert_not_abstract_class(cls):
    abstract_methods = []
    for attr_name in dir(cls):
        attr_val = getattr(cls, attr_name)
        if callable(attr_val):
            try:
                if attr_val.abstract:
                    abstract_methods.append(attr_val.__qualname__)
            except:
                pass
    assert len(abstract_methods) == 0, "\n".join([
        "Class %s is abstract, as following methods are abstract:" % cls.__qualname__] +
        abstract_methods
    )

