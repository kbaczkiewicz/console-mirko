from abc import ABC, abstractmethod

class BaseEvent(ABC):
    @abstractmethod
    def trigger():
        pass
