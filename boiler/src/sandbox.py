import configparser
config = configparser.ConfigParser()
config.read('boiler_config')

con = config['DEFAULT']

print(con['gpio'])