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
def show_class(id):
	gymclass = gymclass_repository.select(id)
	members = gymclass_repository.select_booked_members_for_class(gymclass.id)
	return render_template("/classes/show.html", gymclass=gymclass, members=members)

