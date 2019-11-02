import inspect

class Model:
	connector = None
	table_name = None

	def __new__(cls, *args, **kwargs):
		instance = super(Model, cls).__new__(cls)
		instance.table_name = cls.table_name
		columns = [attr for attr in cls.__dict__ if attr.startswith('col')]
		for col in columns:
			setattr(instance, col, getattr(cls, col))
		return instance
	
	def insert(self):
		raise NotImplementedError

	def to_dict(self):
		raise NotImplementedError

	@property
	def connector(self):
		return Controller.connector
	
	@staticmethod
	def rows(cls, select_query):
		def decorator(select_query, **kwargs):
			results = select_query(**kwargs)
			parameters_name = inspect.getfullargspec(cls.__init__)[0]
			rows = []
			for row in results:
				arguments = [row[p] for p in parameters_name]
				rows.append(globals[cls].__init__(*arguments))
			return rows
		return decorator

	@staticmethod
	def set_connector(connector):
		Model.connector = connector
	
	@classmethod
	def instantiate_rows(cls, rows):
		parameters_name = inspect.getfullargspec(cls.__init__)[0][1:]
		results = []
		for row in rows:
			arguments = [row[p] for p in parameters_name]
			results.append(cls(*arguments))
		return results

