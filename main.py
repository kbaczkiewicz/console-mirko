import os
from consolemirko.appconfig import appconfig
from consolemirko.event import searchevent
from consolemirko import consolemirko

app = consolemirko.ConsoleMirko(os.path.dirname(os.path.realpath(__file__)) + "/config/config.json")
print (app.get_single_comment())
