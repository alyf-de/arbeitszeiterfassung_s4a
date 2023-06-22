// Copyright (c) 2023, ALYF GmbH and contributors
// For license information, please see license.txt

frappe.ui.form.on("Working Time", {
	setup: function (frm) {
		frm.set_query("employee", "erpnext.controllers.queries.employee_query");
		frm.set_query("task", "time_logs", function (doc, cdt, cdn) {
			return {
				filters: {
					project: locals[cdt][cdn].project,
				},
			};
		});
		frm.set_query("project", "time_logs", function (doc, cdt, cdn) {
			return {
				filters: {
					department: doc.department,
				}
			};
		});
	},
});

frappe.ui.form.on("Working Time Log", {
	time_logs_add: function (frm, cdt, cdn) {
		let prev_to_time;
		if (frm.doc.time_logs.length > 1) {
			prev_to_time = frm.doc.time_logs.at(-2).to_time;
		}
		frappe.model.set_value(cdt, cdn, "from_time", prev_to_time || frappe.datetime.now_time(false));
		frappe.model.set_value(cdt, cdn, "to_time", "");  // Otherwise Frappe may overwrite empty values with the current time on save.
	},
});
