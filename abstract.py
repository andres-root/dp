from abc import ABCMeta, abstractmethod, abstractproperty

class MyABC:
    """Absctract base class definition"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def do_something(self, value):
        """Required method"""
    
    @abstractproperty
    def some_property(self):
        """Required property"""
