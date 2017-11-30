from abc import ABCMeta
from . import baseevent

class SearchEvent(baseevent.BaseEvent, metaclass=ABCMeta):
    def trigger(self):
        print ("Search event triggered")
