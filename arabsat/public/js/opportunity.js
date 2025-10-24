
frappe.ui.form.on('Opportunity', {
    refresh(frm) {
        if (!frm.is_new()) {
            frm.add_custom_button(__('Inquiry Form'), () => {
                if (!frm.doc.items || !frm.doc.items.length) {
                    frappe.throw(__('Please select an Item from Items table first.'));
                    return;
                }

                // This automatically calls your API and opens the Inquiry Form
                frappe.model.open_mapped_doc({
                   method: 'arabsat.api.create_inquiry_from_opportunity'
,
                    frm: frm
                });
            }, __('Create'));
        }
    }
}
);

