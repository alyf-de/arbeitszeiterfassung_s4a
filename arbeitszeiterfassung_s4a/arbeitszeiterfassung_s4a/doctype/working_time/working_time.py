# Copyright (c) 2023, ALYF GmbH and contributors
# For license information, please see license.txt

import math

import frappe
from frappe import _
from frappe.model.document import Document

FIVE_MINUTES = 5 * 60
ONE_HOUR = 60 * 60


def get_default_activity():
	return frappe.db.get_single_value("Working Time Settings", "default_activity")


class WorkingTime(Document):
	def before_validate(self):
		self.set_total_times()

	def set_total_times(self):
		(
			self.total_time,
			self.working_time,
			self.project_time,
			self.indicated_break_time,
			self.mandatory_break_time,
			self.break_time,
		) = calculate_total_times(self.time_logs, self.indicated_break_time or 0)

	def validate(self):
		for log in self.time_logs:
			if log.duration and log.duration < 0:
				frappe.throw(_("Please fix negative duration in row {0}").format(log.idx))

			if log.project and not log.task and not log.note:
				frappe.throw(_("Please add task or note in row {0}").format(log.idx))

	def on_submit(self):
		self.create_attendance()
		self.create_timesheets()

	def create_attendance(self):
		if not frappe.db.exists(
			"Attendance", {"employee": self.employee, "attendance_date": self.date, "docstatus": ("!=", 2)}
		):
			HALF_DAY = frappe.get_value("Employee", self.employee, "expected_daily_working_hours") / 2
			OVERTIME_FACTOR = 1.15
			MAX_HALF_DAY = HALF_DAY * OVERTIME_FACTOR * 60 * 60

			attendance = frappe.get_doc(
				{
					"doctype": "Attendance",
					"employee": self.employee,
					"status": "Present" if self.working_time > MAX_HALF_DAY else "Half Day",
					"attendance_date": self.date,
					"working_time": self.name,
					"working_hours": self.working_time / 60 / 60,
				}
			)
			attendance.flags.ignore_permissions = True
			attendance.save()
			attendance.submit()

	def create_timesheets(self):
		for log in self.time_logs:
			if log.duration and log.project:
				costing_rate = get_costing_rate(self.employee)
				hours = math.ceil(log.duration / FIVE_MINUTES) * FIVE_MINUTES / ONE_HOUR
				billing_hours = 0
				if log.billable:
					billing_hours = (
						math.ceil(log.duration * float(log.billable[:-1]) / 100 / FIVE_MINUTES)
						* FIVE_MINUTES
						/ ONE_HOUR
					)

				customer = frappe.get_value(
					"Project",
					log.project,
					["customer"],
				)

				frappe.get_doc(
					{
						"doctype": "Timesheet",
						"time_logs": [
							{
								"is_billable": 1,
								"project": log.project,
								"task": log.task,
								"activity_type": get_default_activity(),
								"base_billing_rate": 0,
								"base_costing_rate": costing_rate,
								"costing_rate": costing_rate,
								"billing_rate": 0,
								"hours": hours,
								"from_time": self.date,
								"billing_hours": billing_hours,
								"description": log.note,
							}
						],
						"parent_project": log.project,
						"customer": customer,
						"employee": self.employee,
						"working_time": self.name,
					}
				).insert()


def get_costing_rate(employee):
	return frappe.get_value(
		"Activity Cost",
		{"activity_type": get_default_activity(), "employee": employee},
		"costing_rate",
	)


def calculate_total_times(time_logs, user_indicated_break_time):
	total_time = 0
	total_working_time = 0
	total_project_time = 0
	total_indicated_break_time = 0

	for log in time_logs:
		log.set_duration()
		duration = log.duration or 0

		if log.is_break:
			total_indicated_break_time += duration
		else:
			total_working_time += duration
			if log.project:
				total_project_time += duration

		total_time += duration

	mandatory_break_time = calcualte_mandatory_break_time(
		total_working_time, total_indicated_break_time
	)
	actual_break_time = max(
		mandatory_break_time, total_indicated_break_time or user_indicated_break_time
	)
	adjusted_working_time = total_time - actual_break_time

	return (
		total_time,
		adjusted_working_time,
		total_project_time,
		total_indicated_break_time or user_indicated_break_time,
		mandatory_break_time,
		actual_break_time,
	)


def calcualte_mandatory_break_time(working_time, break_time):
	if not frappe.db.get_single_value("Working Time Settings", "enforce_mandatory_breaks"):
		return 0
	elif working_time + break_time > 9.75 * ONE_HOUR or working_time > 9 * ONE_HOUR:
		return 45 * 60
	elif working_time + break_time > 6.5 * ONE_HOUR or working_time > 6 * ONE_HOUR:
		return 30 * 60
	else:
		return 0
