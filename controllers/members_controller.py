from flask import Flask, Blueprint, render_template, request, redirect

import repositories.membertype_repository as membertype_repository
import repositories.booking_repository as booking_repository
import repositories.gymclass_repository as gymclass_repository
import repositories.member_repository as member_repository

from models.member import Member
from models.membertype import MemberType
from models.booking import Booking
from models.gymclass import Gymclass


members_blueprint = Blueprint("members", __name__)


@members_blueprint.route("/members")
def members():
	members = member_repository.select_all()
	return render_template("members/index.html", members = members)

@members_blueprint.route("/members/new", methods=['GET'])
def new_member():
	membertypes = membertype_repository.select_all()
	return render_template("members/new.html", membertypes=membertypes)	

@members_blueprint.route("/members/<id>", methods=['GET'])
def show_member(id):
	member = member_repository.select(id)
	if member is None:
		return render_template("/404.html")
	return render_template('members/show.html',
		id = id,
		total_members = member_repository.number_of_members(),
		member = member)

@members_blueprint.route("/members/<id>/edit", methods=['GET'])
def edit_member(id):
	member = member_repository.select(id)
	membertypes = membertype_repository.select_all()
	return render_template('members/edit.html', member=member, membertypes=membertypes)	
	
@members_blueprint.route("/members",  methods=['POST'])
def create_member():
	name = request.form["name"]
	dob = request.form["dob"]
	membertype_id = request.form["membertype_id"]
	membertype = membertype_repository.select(membertype_id)
	member = Member(name, dob, membertype)
	member = member_repository.save(member)
	return redirect(f'/members/{member.id}')

@members_blueprint.route("/members/<id>", methods=['POST'])
def update_member(id):
	name = request.form["name"]
	dob = request.form["dob"]
	membertype_id = request.form["membertype_id"]
	membertype = membertype_repository.select(membertype_id)
	member = Member(name, dob, membertype, id)
	member_repository.update(member)
	return redirect(f'/members/{id}')

@members_blueprint.route("/members/<id>/delete", methods=['POST'])
def delete_member(id):
	member_repository.delete(id)
	return redirect('/members')	