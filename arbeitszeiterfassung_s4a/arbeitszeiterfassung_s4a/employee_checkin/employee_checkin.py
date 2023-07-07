import frappe
from frappe.utils import get_datetime
from datetime import timedelta, datetime

def create_working_time_log(doc, event):
	if doc.log_type == "OUT":
		datetime = get_datetime(doc.time)
		date = datetime.date()
		to_time = datetime.time()
		last_in = frappe.get_all(
			"Employee Checkin",
			filters={
				"log_type": "IN",
				"time": (">", date),		
				"employee": doc.employee,
			},
			order_by="time desc",
			limit=1,
		)
		last_in = frappe.get_doc("Employee Checkin", last_in[0].name)
		from_datetime = get_datetime(last_in.time)
		from_time = from_datetime.time()

		working_time = frappe.get_all(
			"Working Time",
			filters={"employee": doc.employee, "date": date},
			limit=1,
		)
		if not working_time:
			working_time = frappe.new_doc("Working Time")
			working_time.employee = doc.employee
			working_time.date = date
		else:
			working_time = frappe.get_doc("Working Time", working_time[0].name)

		working_time.append(
			"time_logs",
			{
				"from_time": str(from_time),
				"to_time": str(to_time),
			},
		)
		working_time.save()

def switch_checkins_at_midnight():
	"""Create an Employee Checkin of type 'OUT' at 23:59:59 and one of type 'IN' at 00:00:00"""
	current_datetime = datetime.now()
	previous_day = current_datetime - timedelta(days=1)

	for employee_name in frappe.get_all(
		"Employee",
		or_filters=[
			["relieving_date", "is", "not set"],
			["relieving_date", ">", current_datetime.date()]
		],
		pluck="name"
	):
		last_type = frappe.get_all(
			"Employee Checkin",
			order_by="time desc",
			filters={
				"employee": employee_name,
				"time": (">=", previous_day.date())
			},
			limit=1,
			pluck="log_type"
		)
		if last_type and last_type[0] == "IN":
			# create checkin of type OUT at 23:59:59
			new_checkout = frappe.new_doc("Employee Checkin")
			new_checkout.employee = employee.name
			new_checkout.log_type = "OUT"
			new_checkout.time = previous_day.replace(hour=23, minute=59, second=59).strftime("%Y-%m-%d %H:%M:%S")
			new_checkout.save()
			# create checkin of type IN at 00:00:00
			new_checkin = frappe.new_doc("Employee Checkin")
			new_checkin.employee = employee.name
			new_checkin.log_type = "IN"
			new_checkin.time = current_datetime.replace(hour=0, minute=0, second=0).strftime("%Y-%m-%d %H:%M:%S")
			new_checkin.save()
