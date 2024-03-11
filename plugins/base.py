from abc import ABC, abstractmethod


class ArithmeticPlugin(ABC):
    @abstractmethod
    def operation_name(self):
        """
        Returns the name of the arithmetic operation supported by the plugin.
        """
        pass

    @abstractmethod
    def execute(self, x, y):
        """
        Performs the arithmetic operation specified by the plugin and returns the result.
        """
        pass
