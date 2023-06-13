


class Booking():
	def __init__(self, member, gymclass, id=None):
		self.member = member
		self.gymclass = gymclass
		self.id = id
	
	
	def __repr__(self):
		return f"(Booking_{self.id}: {self.member.name}, {self.gymclass.name}, {self.gymclass.event_time}"