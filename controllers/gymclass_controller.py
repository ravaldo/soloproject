from flask import Flask, Blueprint, render_template, request, redirect

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
	return render_template("classes/index.html", gymclasses = gymclasses)


@gymclass_blueprint.route("/classes/<id>")
def show_gymclass(id):
	gymclass = gymclass_repository.select(id)
	if gymclass is None:
		return render_template("/404.html")
	members = gymclass_repository.select_booked_members_for_class(gymclass.id)
	return render_template("/classes/show.html",
		id = id,
		total_classes = gymclass_repository.number_of_classes(),
		gymclass=gymclass,
		members=members)
	
	
@gymclass_blueprint.route("/classes/new")
def new_class():
	return render_template("classes/new.html", slots=Gymclass.time_slots())


@gymclass_blueprint.route("/classes/<id>/edit", methods=['GET'])
def edit_gymclass(id):
	gymclass = gymclass_repository.select(id)
	return render_template('classes/edit.html', slots=Gymclass.time_slots(), gymclass = gymclass)


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