from flask import Flask, Blueprint, render_template, request, redirect

import pdb

import repositories.membertype_repository as membertype_repository
import repositories.booking_repository as booking_repository
import repositories.gymclass_repository as gymclass_repository
import repositories.member_repository as member_repository

from models.member import Member
from models.membertype import MemberType
from models.booking import Booking
from models.gymclass import Gymclass


gymclass_blueprint = Blueprint("gymclass", __name__)


@gymclass_blueprint.route("/classes")
def gymclasses():
	gymclasses = gymclass_repository.select_all()
	occupancy = []
	for g in gymclasses:
		occupancy.append(gymclass_repository.count_bookings_for_class(g.id))
	return render_template("classes/index.html", gymclasses = gymclasses, occupancy=occupancy)


@gymclass_blueprint.route("/classes/<id>")
def show_gymclass(id):
	gymclass = gymclass_repository.select(id)
	if gymclass is None:
		return render_template("/404.html")
	booked_members = gymclass_repository.select_booked_members_for_class(gymclass.id)
	all_members = member_repository.select_all()
	unbooked_members = [m for m in all_members if m.id not in [b.id for b in booked_members]]
	unbooked_members.sort(key=lambda x: x.name)
	return render_template("/classes/show.html",
		id = id,
		total_classes = gymclass_repository.number_of_classes(),
		gymclass=gymclass,
		booked_members=booked_members,
		unbooked_members=unbooked_members )
	
	
@gymclass_blueprint.route("/classes/new")
def new_class():
	return render_template("classes/new.html", slots=Gymclass.time_slots())


@gymclass_blueprint.route("/classes/<id>/edit", methods=['GET'])
def edit_gymclass(id):
	gymclass = gymclass_repository.select(id)
	num_bookings = gymclass_repository.count_bookings_for_class(id)
	return render_template('classes/edit.html', 
		slots=Gymclass.time_slots(), 
		gymclass=gymclass, 
		num_bookings=num_bookings )


@gymclass_blueprint.route("/classes/<id>", methods=['POST'])
def update_gymclass(id):
	name = request.form['name']
	date = request.form['class_date']
	time = request.form['class_time']
	capacity = request.form['capacity']
	gymclass = Gymclass(name, date + " " + time, capacity, id)
	gymclass_repository.update(gymclass)
	return redirect(f"/classes/{id}")
	

@gymclass_blueprint.route("/classes", methods=['POST'])
def create_gymclass():
	name = request.form['name']
	date = request.form['class_date']
	time = request.form['class_time']
	capacity = request.form['capacity']
	gymclass = Gymclass(name, date + " " + time, capacity)
	gymclass = gymclass_repository.save(gymclass)
	return redirect(f"/classes/{gymclass.id}")



@gymclass_blueprint.route("/classes/<id>/delete", methods=['POST'])
def delete_gymclass(id):
	gymclass_repository.delete(id)
	return redirect('/classes')
	
	
@gymclass_blueprint.route("/classes/<id>/remove/<member_id>")
def remove_member_from_class(id, member_id):
	booking_repository.remove_member_from_class(id, member_id)
	return redirect(f'/classes/{id}')


@gymclass_blueprint.route("/classes/<id>/register", methods=['POST'])
def register_members_to_class(id):
	gymclass = gymclass_repository.select(id)
	for member_id in request.form.getlist('memberlist'):
		if gymclass_repository.count_bookings_for_class(gymclass.id) < gymclass.capacity:
			booking_repository.add_member_to_class(member_id, id)
	return redirect(f'/classes/{id}')