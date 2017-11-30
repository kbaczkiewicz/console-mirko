import json


class Config(object):
    def __init__(self, config_path):
        with open(config_path, 'r') as file:
            self._config = json.load(file)

    def get_app_key(self):
        return self._config['app_key']

    def get_app_secret(self):
        return self._config['app_secret']
