import os
from pathlib import Path

from .environment import Environment

from models import UsersModel
from config import *

class TestEnvironment(Environment):
    name = 'test'

    @staticmethod
    def setup(connector):
        connector.execute_sql(f'TRUNCATE TABLE {UsersModel.table_name} RESTART IDENTITY')
        seeds_sql = TestEnvironment.get_seeds_sql()
        connector.execute_sql(seeds_sql)
    
    @staticmethod
    def get_seeds_sql():
        with open(Path(ROOT_DIR, DB_CONFIG['seeds_file'])) as file:
            sql = file.read()
            return sql