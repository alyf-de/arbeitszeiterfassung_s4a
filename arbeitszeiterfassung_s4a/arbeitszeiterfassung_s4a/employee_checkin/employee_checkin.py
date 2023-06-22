import frappe
from frappe.utils import get_datetime


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
