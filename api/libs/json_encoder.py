import json
import datetime
from flask import Flask
from flask_jwt_extended import JWTManager

class JSONEncoder(json.JSONEncoder):
    '''Extend json-encoder class'''

    def default(self, o):
        if isinstance(o, set):
            return list(o)
        elif isinstance(o, datetime.datetime):
            return int(o.timestamp())
        return json.JSONEncoder.default(self, o)