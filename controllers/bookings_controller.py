from flask import Flask, Blueprint, render_template, request, redirect

import repositories.membertype_repository as membertype_repository
import repositories.booking_repository as booking_repository
import repositories.gymclass_repository as gymclass_repository
import repositories.member_repository as member_repository

from models.member import Member
from models.membertype import MemberType
from models.booking import Booking
from models.gymclass import Gymclass


bookings_blueprint = Blueprint("bookings", __name__)


@bookings_blueprint.route("/bookings")
def bookings():
	bookings = booking_repository.select_all()
	return render_template("bookings/index.html", bookings = bookings)


@bookings_blueprint.route("/bookings/new")
def new_booking():
	return render_template("bookings/new.html")


@bookings_blueprint.route("/bookings/<id>")
def show_booking(id):
	booking = bookings_repository.select(id)
	if booking is None:
		return render_template("/bookings/404.html")
#	members = gymclass_repository.select_booked_members_for_class(gymclass.id)
#	return render_template("/classes/show.html",
#		id = id,
#		total_classes = gymclass_repository.number_of_classes(),
#		gymclass=gymclass,
#		members=members)
	
	
@bookings_blueprint.route("/bookings/<id>/edit", methods=['GET'])
def edit_booking(id):
    return render_template('bookings/edit.html', booking = booking)




@bookings_blueprint.route("/bookings", methods=['POST'])
def create_booking():
    return redirect('/bookings')


@bookings_blueprint.route("/bookings/<id>", methods=['POST'])
def update_booking(id):
    return redirect('/bookings')


@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete_booking(id):
    return redirect('/bookings')

