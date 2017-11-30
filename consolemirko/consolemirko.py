from consolemirko.appconfig import appconfig
import wykop


class ConsoleMirko:
    def __init__(self, config_path):
        self._config = appconfig.Config(config_path)
        self._api = wykop.WykopAPI(self._config.get_app_key(), self._config.get_app_secret())
