from flask import Flask
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

from models import Model, UsersModel
from controllers import Controller
from libs import JSONEncoder

from db_connector import Connector
from config import *
from config.environments import Environment

application = Flask(__name__)
application.config['SECRET_KEY'] = SECRET_KEY

# Confirações do JWT
jwt = JWTManager(application)
application.json_encoder = JSONEncoder
application.config['JWT_SECRET_KEY'] = SECRET_KEY
application.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES
application.config["JSON_SORT_KEYS"] = False

# Confirações do Bcrypt
flask_bcrypt = Bcrypt(application)


# Conectado com o banco de dados
db_connector = Connector(
	host=DB_CONFIG['host'],
	database=DB_CONFIG['database'],
	user=DB_CONFIG['user'],
	password=DB_CONFIG['password'],
	migrations_dir=DB_CONFIG['migrations_dir']
)

Model.set_connector(db_connector)

# Deinição das rotas
Controller.set_application(application)
Controller.apply_routes(application)
Controller.set_jwt_rules(jwt)
Controller.set_bcrypt(flask_bcrypt)

# Configurações de ambiente
Environment.set_environment(ENV)
Environment.setup(application, db_connector)

if __name__ == "__main__":
	application.run(host=HOST, port=PORT, debug=DEBUG_MODE)
	db_connector.close()