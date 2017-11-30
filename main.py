import os
from consolemirko.appconfig import appconfig

config = appconfig.Config(os.path.dirname(os.path.realpath(__file__)) + "/config/config.json")
