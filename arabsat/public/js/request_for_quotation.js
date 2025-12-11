

frappe.ui.form.on('Request for Quotation', {
    refresh(frm) {
        frm.add_custom_button(__('Inquiry Form..'), () => {

            //  Make sure Company is selected or show all
            const company_filter = frm.doc.company
                ? ['company', '=', frm.doc.company]
                : null;

            new frappe.ui.form.MultiSelectDialog({
                doctype: 'Inquiry Form',
                target: frm,
                setters: {},
                get_query() {
                    const existing = (frm.doc.items || [])
                        .map(d => d.inquiry_reference)
                        .filter(Boolean);

                    let filters = [
                        ['docstatus', 'in', [0, 1]],
                        ['name', 'not in', existing.length ? existing : ['']]
                     
                    ];

                    //  Add company filter only if company selected
                    if (company_filter) {
                        filters.push(company_filter);
                    }

                    return { filters };
                },
                action(selections) {
                    if (selections && selections.length) {
                        const rfq_name =
                            frm.doc.name && !frm.doc.name.startsWith("new-")
                                ? frm.doc.name
                                : null;

                        frm.call({
                            method: "arabsat.doctype.request_for_quotation.request_for_quotation.get_inquiry_items",
                            args: {
                                // inquiry_names: JSON.stringify(selections),
                                inquiry_names: selections,
                                rfq_name: rfq_name
                            },
                            freeze: true,
                            freeze_message: __("Fetching items..."),
                            callback(r) {
                                if (r.message && r.message.length) {
                                    let added = 0;
                                    (r.message || []).forEach(i => {
                                        const already = (frm.doc.items || []).some(
                                            row =>
                                                row.item_code === i.item_code &&
                                                row.inquiry_reference === i.inquiry_reference
                                        );
                                        if (!already) {
                                            const row = frm.add_child('items');
                                            Object.assign(row, i);
                                            added++;
                                        }
                                    });
                                    frm.refresh_field('items');
                                    frappe.msgprint(__('{0} item(s) fetched successfully.', [added]));
                                } else {
                                    frappe.msgprint(__('No new items found.'));
                                }
                            }
                        });
                    }
                    cur_dialog.hide();
                }
            });
        }, __('Get Items From'));
    }
});
