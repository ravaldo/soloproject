import pdb
from db.run_sql import run_sql
from models.member import Member
from models.membertype import MemberType
import repositories.membertype_repository as membertype_repository
import repositories.booking_repository as booking_repository
import repositories.gymclass_repository as gymclass_repository




def save(member):
	sql = "INSERT INTO members (name, date_of_birth, membertype_id) VALUES (%s, %s, %s) RETURNING id"
	values = [member.name, member.date_of_birth, member.membertype.id]
	results = run_sql(sql, values)
	id = results[0]['id']
	member.id = id
	return member


def select_all():
	members = []
	sql = "SELECT * FROM members ORDER BY name;"
	results = run_sql(sql)
	for result in results:
		membertype = membertype_repository.select(result["membertype_id"])
		member = Member(result["name"], result["date_of_birth"], membertype, result["id"])
		members.append(member)
	return members


def select(id):
	member = None 
	sql = "SELECT * FROM members WHERE id = %s"
	values = [id]
	results = run_sql(sql, values)
	if len(results) > 0:
		result = results[0]
		membertype = membertype_repository.select(result["membertype_id"])
		member = Member(result["name"], result["date_of_birth"], membertype, result["id"])
	return member


def number_of_members(): # presumably faster than doing len(repo.select_all)
	sql = "SELECT COUNT(*) as count FROM members;"
	results = run_sql(sql)
	return results[0]["count"]


def select_booked_classes_for_member(id):
	gymclasses = []
	sql = '''SELECT *
			FROM members
			JOIN bookings
				ON members.id = bookings.member_id
			JOIN classes
				ON bookings.class_id = classes.id
			WHERE members.id = %s
			ORDER BY event_time;
			'''
	values = [id]
	results = run_sql(sql, values)
	for result in results:
		gymclass = gymclass_repository.select(result["class_id"])
		gymclasses.append(gymclass)
	return gymclasses
	

def delete_all():
	sql = "DELETE FROM members"
	run_sql(sql)


def delete(id):
	sql = "DELETE FROM members WHERE id = %s"
	values = [id]
	run_sql(sql, values)


def update(member):
	sql = "UPDATE members SET (name, date_of_birth, membertype_id) = (%s, %s, %s) WHERE id = %s"
	values = [member.name, member.date_of_birth, member.membertype.id, member.id]
	run_sql(sql, values)


