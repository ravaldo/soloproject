import datetime

from models.membertype import MemberType
from models.member import Member
from models.gymclass import Gymclass
from models.booking import Booking

import repositories.membertype_repository as membertype_repository
import repositories.member_repository as member_repository
import repositories.gymclass_repository as gymclass_repository
import repositories.booking_repository as booking_repository

#booking_repository.delete_all()
#gymclass_repository.delete_all()
#member_repository.delete_all()
#membertype_repository.delete_all()
#
#
#membertype_gold = MemberType("GoldStar")
#membertype_silver = MemberType("Silver")
#membertype_platinum = MemberType("Platinum")
#membertype_repository.save(membertype_gold)
#membertype_repository.save(membertype_silver)
#membertype_repository.save(membertype_platinum)

#membertype_gold.name = "Gold"
#membertype_repository.update(membertype_gold)
#assert membertype_repository.select(membertype_gold.id).name == "Gold"
#
#membertype_repository.delete(membertype_platinum.id)
#assert len(membertype_repository.select_all()) == 2
#
#member_1 = Member('Homer Simpson', '22/11/1982', membertype_gold)
#member_repository.save(member_1)
#print(member_1)
#member_1.date_of_birth = datetime.date(1980, 1, 1)
#member_repository.update(member_1)
#print(member_1)
###member_repository.delete_all()
#print(member_repository.select_all())
###member_repository.delete(member_1.id)
#print(member_repository.select_all())
#
#class_1 = Gymclass('CrossFit', "2023-06-18 14:00:00", 20)
#gymclass_repository.save(class_1)
#class_1_retrieve = gymclass_repository.select(class_1.id)
#assert type(class_1_retrieve.event_time) == datetime.datetime
#print(class_1)
#
#class_2 = Gymclass("Cycling", "2023-06-20 16:00:00", 15)
#gymclass_repository.save(class_2)
#class_3 = Gymclass("Yoga", "2023-06-20 19:00:00", 25)
#gymclass_repository.save(class_3)
#class_3.update_time("2023-07-02 18:30:00")
#gymclass_repository.update(class_3)
#print(gymclass_repository.select_all())
#
#booking_1 = Booking(member_1, class_1)
#booking_repository.save(booking_1)
#booking_2 = Booking(member_1, class_3)
#booking_repository.save(booking_2)
#
#
#print(booking_1)
#booking_1.gymclass = class_2
#booking_repository.update(booking_1)
#booking_repository.delete(booking_1.id)
#print(booking_repository.select_all())

#print("\n\n\n")
#print(member_repository.select_booked_classes_for_member(member_1.id))
#print("\n\n\n")
#print(gymclass_repository.select_booked_members_for_class(class_1.id))
#print("\n\n\n")
#print(membertype_repository.select_members_of_membertype(membertype_gold.id))
print(f"total number of classes: {gymclass_repository.number_of_classes()}")


