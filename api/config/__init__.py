import os, sys, datetime
from configparser import ConfigParser

def get_configs(file, section):
	parser = ConfigParser()
	parser.read(file)
	if parser.has_section(section):
		return {param[0]: param[1] for param in parser.items(section)}
	raise Exception('Section {0} not found in the {1} file'.format(section, file))

def get_secret_key(filepath):
	with open(filepath, 'r') as file:
		return file.read()
	raise IOError(f'Can\'t get secret from file: {filepath}')

CONFIG_FILE = 'config/config.ini'

HOST = os.environ.get('HOST', '0.0.0.0')
PORT = int(os.environ.get('PORT', '8080'))
ENV = os.environ.get('ENV', 'development')
DEBUG_MODE = True if ENV in 'development|test' else False

ROOT_DIR = os.path.abspath(os.path.dirname(sys.argv[0]))
DB_CONFIG = get_configs(CONFIG_FILE, 'postgresql')
DB_CONFIG['password'] = DB_CONFIG['password']  if DB_CONFIG['password'] else os.environ.get('POSTGRES_PASSWORD', '')

SECURITY_CONFIG = get_configs(CONFIG_FILE, 'security')
SECRET_KEY_FILE = SECURITY_CONFIG['secret_key_file']
SECRET_KEY = get_secret_key(SECRET_KEY_FILE)

JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=int(SECURITY_CONFIG['jwt_expires_time']))