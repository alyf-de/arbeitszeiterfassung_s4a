from datetime import datetime, timedelta

import frappe
from frappe.utils import get_datetime


def create_working_time_log(doc, event):
	datetime = get_datetime(doc.time)
	checkin_date = datetime.date()
	checkin_time = str(datetime.time())

	working_time = frappe.get_all(
		"Working Time",
		filters={"employee": doc.employee, "date": checkin_date, "docstatus": 0},
		limit=1,
	)
	if not working_time:
		working_time = frappe.new_doc("Working Time")
		working_time.employee = doc.employee
		working_time.date = checkin_date
	else:
		working_time = frappe.get_doc("Working Time", working_time[0].name)

	if doc.log_type == "IN":
		working_time.append(
			"time_logs",
			{
				"from_time": checkin_time,
				"to_time": "",
			},
		)
		if len(working_time.time_logs) > 1 and not working_time.time_logs[-2].to_time:
			working_time.time_logs[-2].to_time = checkin_time

	elif doc.log_type == "OUT":
		if not working_time.time_logs:
			return

		if not working_time.time_logs[-1].to_time:
			working_time.time_logs[-1].to_time = checkin_time
		else:
			working_time.append(
				"time_logs",
				{
					"from_time": working_time.time_logs[-1].to_time,
					"to_time": checkin_time,
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
			new_checkout.employee = employee_name
			new_checkout.log_type = "OUT"
			new_checkout.time = previous_day.replace(hour=23, minute=59, second=59).strftime("%Y-%m-%d %H:%M:%S")
			new_checkout.save()
			# create checkin of type IN at 00:00:00
			new_checkin = frappe.new_doc("Employee Checkin")
			new_checkin.employee = employee_name
			new_checkin.log_type = "IN"
			new_checkin.time = current_datetime.replace(hour=0, minute=0, second=0).strftime("%Y-%m-%d %H:%M:%S")
			new_checkin.save()
