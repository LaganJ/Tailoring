from . import __version__ as app_version

app_name = "tailorpad"
app_title = "Tailorpad"
app_publisher = "White Hat Global"
app_description = "Tailoring Application 2.0"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "rk@whitehatglobal.org"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/tailorpad/css/tailorpad.css"
app_include_css = "/assets/tailorpad/css/hide.css"
app_include_js = "/assets/tailorpad/js/hide_help_menu.js"
# app_include_js = "/assets/tailorpad/js/tailorpad.js"

# include js, css files in header of web template
web_include_css = "/assets/tailorpad/css/tailorpad.css"
# web_include_js = "/assets/tailorpad/js/tailorpad.js"

notification_config = 'tailorpad.custom_folder.notifications.get_notification_config'
setup_wizard_complete = ["tailorpad.install.after_install"]

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "tailorpad/public/scss/website"

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

# Installation
# ------------

# before_install = "tailorpad.install.before_install"
# after_install = "tailorpad.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tailorpad.notifications.get_notification_config"

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

 #override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
 #}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Order": {
		"onload": ["tailorpad.custom_folder.custom_selling.onload_events_so"],
		"validate": ["tailorpad.custom_folder.custom_selling.validate_events_so"],
		"on_update": ["tailorpad.custom_folder.custom_selling.update_events_so"],
		"on_submit": ["tailorpad.custom_folder.custom_selling.submit_event", "tailorpad.custom_folder.custom_buying.submit_event", "tailorpad.custom_folder.custom_account.submit_event"],
		"on_cancel": ["tailorpad.custom_folder.custom_selling.cancel_event", "tailorpad.custom_folder.custom_buying.cancel_event", "tailorpad.custom_folder.custom_account.cancel_event"],
		"before_cancel": ["tailorpad.custom_folder.custom_buying.before_cancel_event"]
	},
	"Sales Invoice": {
		"on_submit": ["tailorpad.custom_folder.custom_selling.update_events_si"]
	},
	"Item": {
		"validate": ["tailorpad.custom_folder.custom_item_details.validate_events"],
		"on_update": ["tailorpad.custom_folder.custom_item_details.update_events"]
	},
	"Customer": {
		"onload": ["tailorpad.custom_folder.custom_selling.customer_onload_events"],
		"validate": ["tailorpad.custom_folder.custom_selling.customer_validate_events"],
		"on_update": ["tailorpad.custom_folder.custom_selling.customer_update_events"]
	},
	"Stock Entry": {
		"on_update": ["tailorpad.custom_folder.custom_stock.stock_events"],
		"on_submit": ["tailorpad.custom_folder.custom_stock.onsubmit_stock_events"],
	},
	"Quality Inspection": {
		"on_submit": ["tailorpad.custom_folder.custom_manufacturing.qi_events"],
		"on_cancel": ["tailorpad.custom_folder.custom_manufacturing.qi_cancel_events"]
	},
	"Quotation": {
		"on_update": ["tailorpad.custom_folder.custom_selling.update_events_qo"]
	},
	"Operation": {
		"on_update": ["tailorpad.custom_folder.custom_item_details.update_op_events"]
	},
	"Purchase Order": {
		"on_update": ["tailorpad.custom_folder.custom_item_details.update_po_events"]
	},
	"Purchase Receipt": {
		"on_submit": ["tailorpad.custom_folder.custom_item_details.update_pr_events"]
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"tailorpad.tasks.all"
# 	],
# 	"daily": [
# 		"tailorpad.tasks.daily"
# 	],
# 	"hourly": [
# 		"tailorpad.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tailorpad.tasks.weekly"
# 	]
# 	"monthly": [
# 		"tailorpad.tasks.monthly"
# 	]
# }

doctype_js = {
    "User": ["custom_scripts/user.js"],
    "Item": ["custom_scripts/item.js"],
	"Sales Order": ["custom_scripts/sales_order.js"],
	"Quotation": ["custom_scripts/quotation.js"],
	"Sales Invoice": ["custom_scripts/sales_invoice.js"],
	"Customer": ["custom_scripts/customer.js"],
	"Purchase Order": ["custom_scripts/purchase_order.js"],
	"Stock Entry": ["custom_scripts/stock_entry.js"],
	"Production Order": ["custom_scripts/production_order.js"],
	"Employee": ["custom_scripts/employee.js"],
	"Delivery Note": ["custom_scripts/delivery_note.js"]

}


# Testing
# -------

# before_tests = "tailorpad.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tailorpad.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "tailorpad.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"tailorpad.auth.validate"
# ]
fixtures = [
	 "Custom Field",
	 "Property Setter",
	 "Workspace",
	 "Client Script"
	]