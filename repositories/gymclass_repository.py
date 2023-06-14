from db.run_sql import run_sql
from models.gymclass import Gymclass

import repositories.gymclass_repository as gymclass_repository
import repositories.member_repository as member_repository


def save(gymclass):
	sql = "INSERT INTO classes (name, event_time, capacity) VALUES (%s, %s, %s) RETURNING id"
	values = [gymclass.name, gymclass.event_time, gymclass.capacity]
	results = run_sql(sql, values)
	id = results[0]['id']
	gymclass.id = id
	return gymclass


def select_all():
	gymclasses = []
	sql = "SELECT * FROM classes"
	results = run_sql(sql)
	for result in results:
		gymclass = Gymclass(result["name"], result["event_time"], result["capacity"], result['id'])
		gymclasses.append(gymclass)
	return gymclasses


def select(id):
	gymclass = None 
	sql = "SELECT * FROM classes WHERE id = %s"
	values = [id]
	results = run_sql(sql, values)
	if len(results) > 0: 
		result = results[0]
		gymclass = Gymclass(result["name"], result["event_time"], result["capacity"], result['id'])
	return gymclass
	

def number_of_classes():
	sql = "SELECT COUNT (*) FROM classes;"
	results = run_sql(sql)
	return results[0]["count"]
	
def select_booked_members_for_class(id):
	members = []
	sql = '''SELECT *
			FROM classes
			JOIN bookings
			    ON classes.id = bookings.class_id
			JOIN members
			    ON members.id = bookings.member_id
			WHERE classes.id = %s
			ORDER BY members.name;
			'''
	values = [id]
	results = run_sql(sql, values)
	for result in results:
		member = member_repository.select(result["member_id"])
		members.append(member)
	return members


def count_bookings_for_class(id):
	sql = '''SELECT COUNT(*)
			FROM classes
			JOIN bookings ON classes.id = bookings.class_id
			JOIN members ON members.id = bookings.member_id
			WHERE classes.id = %s;
			'''
	values = [id]
	results = run_sql(sql, values)
	return results[0]["count"]
	

def delete_all():
	sql = "DELETE FROM classes"
	run_sql(sql)


def delete(id):
	sql = "DELETE FROM classes WHERE id = %s"
	values = [id]
	run_sql(sql, values)


def update(gymclass):
	sql = "UPDATE classes SET (name, event_time, capacity) = (%s, %s, %s) WHERE id = %s"
	values = [gymclass.name, gymclass.event_time, gymclass.capacity, gymclass.id]
	run_sql(sql, values)


