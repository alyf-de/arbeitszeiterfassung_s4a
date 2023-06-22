from . import __version__ as app_version

app_name = "arbeitszeiterfassung_s4a"
app_title = "Arbeitszeiterfassung S4A"
app_publisher = "ALYF GmbH"
app_description = "Arbeitszeiterfassung und Gleitzeit aus Employee Checkin"
app_email = "hallo@alyf.de"
app_license = "GPLv3"

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
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "arbeitszeiterfassung_s4a.utils.jinja_methods",
#	"filters": "arbeitszeiterfassung_s4a.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "arbeitszeiterfassung_s4a.install.before_install"
# after_install = "arbeitszeiterfassung_s4a.install.after_install"

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
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"arbeitszeiterfassung_s4a.tasks.all"
#	],
#	"daily": [
#		"arbeitszeiterfassung_s4a.tasks.daily"
#	],
#	"hourly": [
#		"arbeitszeiterfassung_s4a.tasks.hourly"
#	],
#	"weekly": [
#		"arbeitszeiterfassung_s4a.tasks.weekly"
#	],
#	"monthly": [
#		"arbeitszeiterfassung_s4a.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "arbeitszeiterfassung_s4a.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "arbeitszeiterfassung_s4a.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "arbeitszeiterfassung_s4a.task.get_dashboard_data"
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
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"arbeitszeiterfassung_s4a.auth.validate"
# ]
