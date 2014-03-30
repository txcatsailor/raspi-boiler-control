import configparser

def prop(tag):
    config = configparser.ConfigParser()
    config.read('boiler_config')
    con = config['DEFAULT']
    
    return con[tag]