import ipaddress
import os

def db_uri_from_config(config):
    if not config:
        raise ValueError('No config options object specified')
    
    db_type = config['sqlalchemy']['db_backend']

    if db_type == 'sqlite':
        # NOTE: since we're reading a ConfigParser object, which stores all
        # option values as strings, check against the string 'True' since the
        # truthiness of the string 'False' is also True. lol.
        if config['sqlite']['mem_db'] == 'True':
            uri = '/:memory:'
        else:
            uri = os.path.expanduser(config['sqlite3']['db_file'])
    elif db_type == 'mysql':
        # ensure the ip address specified in the configuration is valid
        ip_str = config['mysql']['db_ip']
        try:
            ip = ipaddress.ip_address(ip_str)
        except ValueError:
            # allow 'localhost' to be used as the database ip
            if ip_str != 'localhost':
                raise

        # ensure the specified port is valid
        port = int(config['mysql']['db_port'])
        if port < 0 or port > 65353:
            raise ValueError('Invalid port specified: %d' % port)
        
        uri = '%s:%d' % (ip_str, port)

    # if the db_api value to use is not empty, append a plus to the beginning
    dbapi_str = config['sqlalchemy']['db_api'] 
    if dbapi_str:
        dbapi_str = '+%s' % dbapi_str

    return '%s%s://%s' % (db_type, dbapi_str, uri)
