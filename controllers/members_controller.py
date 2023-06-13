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
    return render_template("members/new.html")

@members_blueprint.route("/members",  methods=['POST'])
def create_member():
    return redirect('/members')

@members_blueprint.route("/members/<id>", methods=['GET'])
def show_member(id):
    return render_template('members/show.html', member = member)

@members_blueprint.route("/members/<id>/edit", methods=['GET'])
def edit_member(id):
    return render_template('members/edit.html', member = member)

@members_blueprint.route("/members/<id>", methods=['POST'])
def update_member(id):
    return redirect('/members')

@members_blueprint.route("/members/<id>/delete", methods=['POST'])
def delete_member(id):
    return redirect('/members')