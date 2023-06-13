from db.run_sql import run_sql
import pdb

from models.membertype import MemberType
import repositories.member_repository as member_repository



def save(membertype):
	sql = "INSERT INTO membertypes (name) VALUES (%s) RETURNING id"
	values = [membertype.name]
	results = run_sql(sql, values)
	id = results[0]['id']
	membertype.id = id
	return membertype


def select_all():
	membertypes = []
	sql = "SELECT * FROM membertypes"
	results = run_sql(sql)
	for result in results:
		membertype = MemberType(result["name"], result["id"])
		membertypes.append(membertype)
	return membertypes


def select(id):
	membertype = None 
	sql = "SELECT * FROM membertypes WHERE id = %s"
	values = [id]
	results = run_sql(sql, values)
	if len(results) > 0:
		result = results[0]
	membertype = MemberType(result["name"], result["id"])
	return membertype
	

def select_members_of_membertype(id):
	members = []
	sql = '''SELECT members.*
			FROM members
			JOIN membertypes
			    ON membertypes.id = members.membertype_id
			WHERE members.membertype_id = %s;
		'''	
	values = [id]
	results = run_sql(sql, values)
	for result in results:
#		pdb.set_trace()
		member = member_repository.select(result["id"])
		members.append(member)
	return members


def delete_all():
	sql = "DELETE FROM membertypes"
	run_sql(sql)


def delete(arg):
	sql = "DELETE FROM membertypes WHERE id = %s"
	if type(arg) == MemberType:
		values = [arg.id]
	else:
		values = [arg]
	run_sql(sql, values)


def update(membertype):
	sql = "UPDATE membertypes SET name = %s WHERE id = %s"
	values = [membertype.name, membertype.id]
	run_sql(sql, values)
