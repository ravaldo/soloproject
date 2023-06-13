from models.membertype import MemberType
import datetime as dt
from dateutil.parser import parse

	
class Member():
	def __init__(self, name, dob, membertype, id=None):
		if type(dob) == str:
			dob = parse(dob, dayfirst=True).date() # use dateutil.parser to convert string to date object
		self.name = name
		self.date_of_birth = dob
		self.membertype = membertype
		self.id = id
	
	def __repr__(self):
		return f"(Member_{self.id}: {self.name}, {self.date_of_birth}, {self.membertype.name})"
	