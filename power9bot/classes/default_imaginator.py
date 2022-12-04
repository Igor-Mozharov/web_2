from abc import ABC, abstractmethod


class DefaultImaginator(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def imagination(self):
        pass
