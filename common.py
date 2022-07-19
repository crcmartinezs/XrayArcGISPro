import yaml

_config = None

def config():
    global _config

    if _config is None:
        with open("config.yaml") as file:
            _config = yaml.load(file, Loader=yaml.FullLoader)

        return _config
