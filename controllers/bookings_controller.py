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


