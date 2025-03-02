
import threading
class DbConn:
	__instance = None

	def __new__(cls, *args, **kwargs): # __new__ method gets called before __init__ method
		if cls.__instance is None:
			print("new object getting created...")
			cls.__instance = super().__new__(cls)
		return cls.__instance

print("creation count: 1")
s1 = DbConn()

print("creation count: 2")
s1 = DbConn()


# Threading
class DbConnTh:
	__instance = None
	__lock = threading.Lock()

	def __new__(cls, *args, **kwargs): # __new__ method gets called before __init__ method
		if cls.__instance is None:
			with cls.__lock:
				if cls.__instance is None:
					print("new object getting created...")
					cls.__instance = super().__new__(cls)
		return cls.__instance