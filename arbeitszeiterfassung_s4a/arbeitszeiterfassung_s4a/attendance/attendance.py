import frappe
from erpnext.setup.doctype.employee.employee import get_holiday_list_for_employee
from erpnext.setup.doctype.holiday_list.holiday_list import is_holiday
from frappe.utils import add_days, getdate
from hrms.hr.doctype.attendance.attendance import (
	get_unmarked_days,
	mark_bulk_attendance,
)


def before_validate(doc, event=None):
	holiday_list = get_holiday_list_for_employee(doc.employee)
	attendance_on_holiday = is_holiday(holiday_list, doc.attendance_date)

	if attendance_on_holiday:
		doc.expected_working_hours = 0
	elif doc.leave_type:
		# Leave on a holiday does not count as working.
		# If leave type is partially paid, record a fraction of the expected
		# working time as working time.
		leave_type = frappe.get_doc("Leave Type", doc.leave_type)
		if leave_type.is_ppl:
			doc.working_hours = (
				doc.expected_working_hours
				* leave_type.fraction_of_daily_salary_per_leave
			)

	if not doc.working_hours:
		doc.working_hours = 0

	doc.flexitime = doc.working_hours - doc.expected_working_hours


def mark_absent_attendance():
	to_date = getdate()
	from_date = add_days(to_date, -7)
	for employee in frappe.get_all(
		"Employee",
		or_filters=[
			["relieving_date", ">", from_date],
			["relieving_date", "is", "not set"],
		],
		pluck="name",
	):
		unmarked_days = get_unmarked_days(
			employee, from_date, to_date, exclude_holidays=1
		)
		if unmarked_days:
			mark_bulk_attendance(
				{
					"employee": employee,
					"status": "Absent",
					"unmarked_days": unmarked_days,
				}
			)
