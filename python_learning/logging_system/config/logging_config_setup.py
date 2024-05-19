import os
import yaml
import logging.config
import logging
import coloredlogs
import traceback


def setup_logging(default_path='config/logging_config.yaml', default_level=logging.INFO, env_key='LOG_CFG'):
    """
    参考：https://gist.github.com/kingspp/9451566a5555fb022215ca2b7b802f19
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt', encoding="utf-8") as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
                coloredlogs.install()
            except Exception:
                print('Error in Logging Configuration. Using default configs!')
                traceback.print_exc()
                logging.basicConfig(level=default_level)
                coloredlogs.install(level=default_level)
    else:
        logging.basicConfig(level=default_level)
        coloredlogs.install(level=default_level)
        print('Failed to load configuration file. Using default configs')
