frappe.ui.form.on('Request for Quotation', {
    refresh(frm) {
        // if (!frm.is_new()) {
            frm.add_custom_button(__('Inquiry Form..'), () => {
                // frappe.prompt([
                                      new frappe.ui.form.MultiSelectDialog({
                                doctype: 'Inquiry Form',
                                target: frm,
                                setters: {},
                                get_query() {
                                    // return { filters: { docstatus: 1 } };
                                    return {
                                        filters: {
                                            docstatus: ['in', [0, 1]]
                                        }
                                    };
                                },
                                action(selections) {
                                    if (selections && selections.length) {
                                        frm.call({
                                            method: "arabsat.doctype.request_for_quotation.request_for_quotation.get_inquiry_items",
                                            args: { inquiry_names: JSON.stringify(selections) },
                                            callback(r) {
                                                if (r.message) {
                                                    (r.message || []).forEach(i => {
                                                        let row = frm.add_child('items');
                                                        Object.assign(row, i);
                                                    });
                                                    frm.refresh_field('items');
                                                    frappe.msgprint(__('Items fetched successfully.'));
                                                }
                                            }
                                        });
                                    }
                                    cur_dialog.hide();
                                }
                            });
                // //     {
                // //         label: 'Allow Multiple',
                // //         fieldname: 'multiple',
                // //         fieldtype: 'Check',
                // //         default: 0
                // //     },
                // //     {
                // //         label: 'Inquiry Reference',
                // //         fieldname: 'inquiry',
                // //         fieldtype: 'Link',
                // //         options: 'Inquiry Form',
                // //         reqd: 1,
                // //         depends_on: 'eval:!doc.multiple'
                // //     }
                // // ],
                // //     function (values) {
  
                        // if (values.multiple) {
                        //     new frappe.ui.form.MultiSelectDialog({
                        //         doctype: 'Inquiry Form',
                        //         target: frm,
                        //         setters: {},
                        //         get_query() {
                        //             // return { filters: { docstatus: 1 } };
                        //             return {
                        //                 filters: {
                        //                     docstatus: ['in', [0, 1]]
                        //                 }
                        //             };
                        //         },
                        //         action(selections) {
                        //             if (selections && selections.length) {
                        //                 frm.call({
                        //                     method: "arabsat.doctype.request_for_quotation.request_for_quotation.get_inquiry_items",
                        //                     args: { inquiry_names: JSON.stringify(selections) },
                        //                     callback(r) {
                        //                         if (r.message) {
                        //                             (r.message || []).forEach(i => {
                        //                                 let row = frm.add_child('items');
                        //                                 Object.assign(row, i);
                        //                             });
                        //                             frm.refresh_field('items');
                        //                             frappe.msgprint(__('Items fetched successfully.'));
                        //                         }
                        //                     }
                        //                 });
                        //             }
                        //             cur_dialog.hide();
                        //         }
                        //     });
                        // } else {
                        //     frm.call({
                        //         method: "arabsat.doctype.request_for_quotation.request_for_quotation.get_inquiry_items",
                        //         args: { inquiry_names: JSON.stringify([values.inquiry]) },
                        //         callback(r) {
                        //             if (r.message) {
                        //                 (r.message || []).forEach(i => {
                        //                     let row = frm.add_child('items');
                        //                     Object.assign(row, i);
                        //                 });
                        //                 frm.refresh_field('items');
                        //                 frappe.msgprint(__('Items fetched successfully.'));
                        //             }
                        //         }
                        //     });
                        // }
                // //     },
                //     __('Get Items from Inquiry Form'),
                //     __('Fetch Items'));
            }, __('Get Items From'));
        }
    }
); 