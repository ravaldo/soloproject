from dateutil.parser import parse


class Gymclass():
	def __init__(self, name, event_time, capacity, id=None):
		if type(event_time) == str:
			event_time = parse(event_time, dayfirst=True)
		self.name = name
		self.event_time = event_time
		self.capacity = capacity
		self.id = id
	
	def update_time(self, string):
		self.event_time = parse(string, dayfirst=True)
	
	def __repr__(self):
		return f"(Gymclass_{self.id}: {self.name}, {self.capacity} capacity, {self.event_time})"
		