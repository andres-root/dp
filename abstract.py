from abc import ABCMeta, abstractmethod, abstractproperty

class MyABC(object):
    """Absctract base class definition"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def do_something(self, value):
        """Required method"""
    
    @abstractproperty
    def some_property(self):
        """Required property"""


class MyClass(MyABC):
    def __init__(self, value=None):
        self._myprop = value
    
    def do_something(self, value):
        self._myprop *= 2 + value
    
    @property
    def some_property(self):
        return self._myprop
