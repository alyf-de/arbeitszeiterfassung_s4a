app_name = "arbeitszeiterfassung_s4a"
app_title = "Arbeitszeiterfassung S4A"
app_publisher = "ALYF GmbH"
app_description = "Arbeitszeiterfassung und Gleitzeit aus Employee Checkin"
app_email = "hallo@alyf.de"
app_license = "GPLv3"
required_apps = ["erpnext", "hrms"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/arbeitszeiterfassung_s4a/css/arbeitszeiterfassung_s4a.css"
# app_include_js = "/assets/arbeitszeiterfassung_s4a/js/arbeitszeiterfassung_s4a.js"

# include js, css files in header of web template
# web_include_css = "/assets/arbeitszeiterfassung_s4a/css/arbeitszeiterfassung_s4a.css"
# web_include_js = "/assets/arbeitszeiterfassung_s4a/js/arbeitszeiterfassung_s4a.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "arbeitszeiterfassung_s4a/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "arbeitszeiterfassung_s4a.utils.jinja_methods",
# 	"filters": "arbeitszeiterfassung_s4a.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "arbeitszeiterfassung_s4a.install.before_install"
after_install = "arbeitszeiterfassung_s4a.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "arbeitszeiterfassung_s4a.uninstall.before_uninstall"
# after_uninstall = "arbeitszeiterfassung_s4a.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "arbeitszeiterfassung_s4a.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Attendance": {
		"before_validate": "arbeitszeiterfassung_s4a.arbeitszeiterfassung_s4a.attendance.attendance.before_validate",
	},
	"Employee Checkin": {
		"after_insert": "arbeitszeiterfassung_s4a.arbeitszeiterfassung_s4a.employee_checkin.employee_checkin.create_working_time_log",
	},
}

# Scheduled Tasks
# ---------------
scheduler_events = {
	"cron": {
		"55 23 * * 7": [  # At 23:55 on Sunday
			"arbeitszeiterfassung_s4a.arbeitszeiterfassung_s4a.attendance.attendance.mark_absent_attendance",
		],
	},
	"cron": {
		"0 0 * * 2-6": [  # At 00:00 on every day-of-week from Tuesday through Saturday.
			"arbeitszeiterfassung_s4a.arbeitszeiterfassung_s4a.employee_checkin.employee_checkin.switch_checkins_at_midnight",
		],
	},
}

# Testing
# -------

# before_tests = "arbeitszeiterfassung_s4a.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "arbeitszeiterfassung_s4a.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "arbeitszeiterfassung_s4a.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["arbeitszeiterfassung_s4a.utils.before_request"]
# after_request = ["arbeitszeiterfassung_s4a.utils.after_request"]

# Job Events
# ----------
# before_job = ["arbeitszeiterfassung_s4a.utils.before_job"]
# after_job = ["arbeitszeiterfassung_s4a.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"arbeitszeiterfassung_s4a.auth.validate"
# ]

arbeitszeit_property_setters = [
	# ("Timesheet Detail", "is_billable", "default", "1", "Small Text"),
	# ("Timesheet Detail", "activity_type", "default", "Montage", "Small Text"),
	("Attendance", "working_hours", "default", "0", "Small Text"),
]

arbeitszeit_custom_fields = {
	"Employee": [
		{
			"fieldname": "expected_daily_working_hours",
			"fieldtype": "Float",
			"insert_after": "attendance_device_id",
			"label": "Expected Daily Working Hours",
			"translatable": 0,
		},
	],
	"Attendance": [
		{
			"fieldname": "expected_working_hours",
			"fieldtype": "Float",
			"insert_after": "working_hours",
			"label": "Expected Working Hours",
			"read_only": 1,
			"default": "0",
			"translatable": 0,
			"fetch_from": "employee.expected_daily_working_hours",
		},
		{
			"fieldname": "flexitime",
			"fieldtype": "Float",
			"insert_after": "expected_working_hours",
			"label": "Flexitime",
			"read_only": 1,
			"default": "0",
			"translatable": 0,
		},
		{
			"fieldname": "working_time",
			"label": "Working Time",
			"fieldtype": "Link",
			"options": "Working Time",
			"insert_after": "company",
			"translatable": 0,
			"read_only": 1,
		},
	],
	"Timesheet": [
		{
			"fieldname": "working_time",
			"label": "Working Time",
			"fieldtype": "Link",
			"options": "Working Time",
			"insert_after": "project",
			"translatable": 0,
			"read_only": 1,
		}
	],
}
