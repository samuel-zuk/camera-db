from configparser import ConfigParser
import os
import sys


DEFAULTS = {
    'sqlalchemy': {
        'db_backend': 'sqlite3',
        'db_api': 'pysqlite'
    },
    'sqlite3': {
        'db_file': '~/.camera_db/camdb.db',
        'mem_db': False
    },
    'mysql': {
        'db_ip': '127.0.0.1',
        'db_port': '12345'
    }
}


def get_config():
    # initialize the configparser object with default values
    config = ConfigParser()
    config.read_dict(DEFAULTS)

    # check to see if the config file location is specified in env vars
    config_file = os.environ.get('CDB_CONFIG_FILE', None)

    if config_file is not None:
        if not os.access(config_file, os.F_OK):
            raise FileNotFoundError('Invalid path for config file %s' %
                                    config_file)
    else:
        # if not, check if config.conf exists in the following order:
        # 1) /etc/camera_db/config.conf
        # 2) ~/.camera_db/config.conf
        # 3) ./config.conf
        for path in ('/etc/camera_db/config.conf',
                  os.path.join(os.path.expanduser('~'), 'config.conf'),
                  os.path.join(os.getcwd(), 'config.conf')):
            if os.access(path, os.F_OK):
                config_file = path
                break
        # if we still have not found a config file, throw an exception.
        if config_file is None:
            raise FileNotFoundError('Could not find config file')

    # make sure we can read the file
    if not os.access(config_file, os.R_OK):
        raise PermissionError('Permissions denied on config file %s' %
                              config_file)

    # we've found the config file, read values from it and get out
    with open(config_file, 'r') as f:
        config.read_file(f)

    return config
