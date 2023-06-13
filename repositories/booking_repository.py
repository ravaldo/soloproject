from db.run_sql import run_sql
from models.member import Member
from models.gymclass import Gymclass
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.gymclass_repository as gymclass_repository


def save(booking):
	sql = "INSERT INTO bookings (member_id, class_id) VALUES (%s, %s) RETURNING id"
	values = [booking.member.id, booking.gymclass.id]
	results = run_sql(sql, values)
	id = results[0]['id']
	booking.id = id


def select_all():
	bookings = []
	sql = "SELECT * FROM bookings"
	results = run_sql(sql)
	for result in results:
		member = member_repository.select(result['member_id'])
		gymclass = gymclass_repository.select(result['class_id'])
		booking = Booking(member, gymclass, result["id"])
		bookings.append(booking)
	return bookings


def select(id):
	booking = None 
	sql = "SELECT * FROM bookings WHERE id = %s"
	values = [id]
	results = run_sql(sql, values)
	if len(results) > 0:
		result = results[0]
		member = member_repository.select(result['member_id'])
		gymclass = gymclass_repository.select(result['class_id'])
		booking = Booking(member, gymclass, result["id"])
	return booking


def delete_all():
	sql = "DELETE FROM bookings"
	run_sql(sql)


def delete(id):
	sql = "DELETE FROM bookings WHERE id = %s"
	values = [id]
	run_sql(sql, values)


def update(booking):
	sql = "UPDATE bookings SET (member_id, class_id) = (%s, %s) WHERE id = %s"
	values = [booking.member.id, booking.gymclass.id, booking.id]
	run_sql(sql, values)


