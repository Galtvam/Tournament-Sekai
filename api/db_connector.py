import os
import traceback
import psycopg2
import psycopg2.extras

class Connector:
	MIGRATIONS_STATE_FILE = 'migrations_state'

	def __init__(self, host, database, user, password, migrations_dir=None):
		self._host = host
		self._database = database
		self._user = user
		self._password = password
		
		self._conn = None
		
		self._migrations_dir = migrations_dir
		self._migrations = self._get_migrations(migrations_dir)
		self._loaded_migrations = self._get_loaded_migrations(migrations_dir)
		self._load_migrations(self._migrations, self._loaded_migrations)

	@property	
	def connection(self):
		if self._conn is None:
			self._connect()
		return self._conn

	def execute_sql(self, sql, *args):
		cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(sql, *args)
		result = []
		try:
			result = cursor.fetchall() if cursor.rowcount > 0 else []
		except psycopg2.ProgrammingError:
			pass
		finally:
			cursor.close()
			return [dict(row) for row in result]
	
	@property
	def migration_state_file(self):
		return os.path.abspath(os.path.join(self._migrations_dir, Connector.MIGRATIONS_STATE_FILE))
	
	def close(self):
		if self._conn is not None:
			self._conn.close()

	def _connect(self):
		self._conn = psycopg2.connect(host=self._host, database=self._database, user=self._user, password=self._password)
		self._conn.set_session(autocommit=True)

	def _get_migrations(self, migrations_dir):
		migrations = os.listdir(migrations_dir)
		migrations_dir = os.path.abspath(migrations_dir)
		migration_files = sorted([os.path.join(migrations_dir, file) for file in migrations])
		if self.migration_state_file in migration_files:
			migration_files.remove(self.migration_state_file)
		return migration_files
	
	def _get_loaded_migrations(self, migrations_dir):
		if os.path.exists(self.migration_state_file):
			with open(self.migration_state_file, 'r') as file:
				return file.read().split('|')[:-1]
		return []
	
	def _load_migrations(self, migration_files, loaded_migrations):
		for filepath in migration_files:
			basename = os.path.basename(filepath)
			if basename not in loaded_migrations:
				with open(filepath, 'r') as file:
					sql = file.read()
					self.execute_sql(sql)
					self._add_loaded_migration(basename)
	
	def _add_loaded_migration(self, migration):
		with open(self.migration_state_file, 'a') as file:
			return file.write(f'{migration}|')

	def _run_setup(self, setup_file):
		if setup_file:
			with open(setup_file, 'r') as file:
				sql = file.read()
				self.execute_sql(sql)
