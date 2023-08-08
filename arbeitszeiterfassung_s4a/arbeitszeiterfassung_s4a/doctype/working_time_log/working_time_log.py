# Copyright (c) 2023, ALYF GmbH and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.utils import time_diff_in_seconds
from frappe.utils.data import to_timedelta


class WorkingTimeLog(Document):
	def set_duration(self):
		if self.from_time and self.to_time:
			self.duration = time_diff_in_seconds(to_timedelta(self.to_time), to_timedelta(self.from_time))
