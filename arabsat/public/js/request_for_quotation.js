// frappe.ui.form.on('Request for Quotation', {
//     refresh(frm) {
//         // if (!frm.is_new()) {
//             frm.add_custom_button(__('Inquiry Form..'), () => {
//                 // frappe.prompt([
//                                       new frappe.ui.form.MultiSelectDialog({
//                                 doctype: 'Inquiry Form',
//                                 target: frm,
//                                 setters: {},
//                                 get_query() {
//                                     // return { filters: { docstatus: 1 } };
//                                     return {
//                                         filters: {
//                                             docstatus: ['in', [0, 1]]
//                                         }
//                                     };
//                                 },
//                                 action(selections) {
//                                     if (selections && selections.length) {
//                                         frm.call({
//                                             method: "arabsat.doctype.request_for_quotation.request_for_quotation.get_inquiry_items",
//                                             args: { inquiry_names: JSON.stringify(selections) },
//                                             callback(r) {
//                                                 if (r.message) {
//                                                     (r.message || []).forEach(i => {
//                                                         let row = frm.add_child('items');
//                                                         Object.assign(row, i);
//                                                     });
//                                                     frm.refresh_field('items');
//                                                     frappe.msgprint(__('Items fetched successfully.'));
//                                                 }
//                                             }
//                                         });
//                                     }
//                                     cur_dialog.hide();
//                                 }
//                             });
//                 // //     {
//                 // //         label: 'Allow Multiple',
//                 // //         fieldname: 'multiple',
//                 // //         fieldtype: 'Check',
//                 // //         default: 0
//                 // //     },
//                 // //     {
//                 // //         label: 'Inquiry Reference',
//                 // //         fieldname: 'inquiry',
//                 // //         fieldtype: 'Link',
//                 // //         options: 'Inquiry Form',
//                 // //         reqd: 1,
//                 // //         depends_on: 'eval:!doc.multiple'
//                 // //     }
//                 // // ],
//                 // //     function (values) {
  
//                         // if (values.multiple) {
//                         //     new frappe.ui.form.MultiSelectDialog({
//                         //         doctype: 'Inquiry Form',
//                         //         target: frm,
//                         //         setters: {},
//                         //         get_query() {
//                         //             // return { filters: { docstatus: 1 } };
//                         //             return {
//                         //                 filters: {
//                         //                     docstatus: ['in', [0, 1]]
//                         //                 }
//                         //             };
//                         //         },
//                         //         action(selections) {
//                         //             if (selections && selections.length) {
//                         //                 frm.call({
//                         //                     method: "arabsat.doctype.request_for_quotation.request_for_quotation.get_inquiry_items",
//                         //                     args: { inquiry_names: JSON.stringify(selections) },
//                         //                     callback(r) {
//                         //                         if (r.message) {
//                         //                             (r.message || []).forEach(i => {
//                         //                                 let row = frm.add_child('items');
//                         //                                 Object.assign(row, i);
//                         //                             });
//                         //                             frm.refresh_field('items');
//                         //                             frappe.msgprint(__('Items fetched successfully.'));
//                         //                         }
//                         //                     }
//                         //                 });
//                         //             }
//                         //             cur_dialog.hide();
//                         //         }
//                         //     });
//                         // } else {
//                         //     frm.call({
//                         //         method: "arabsat.doctype.request_for_quotation.request_for_quotation.get_inquiry_items",
//                         //         args: { inquiry_names: JSON.stringify([values.inquiry]) },
//                         //         callback(r) {
//                         //             if (r.message) {
//                         //                 (r.message || []).forEach(i => {
//                         //                     let row = frm.add_child('items');
//                         //                     Object.assign(row, i);
//                         //                 });
//                         //                 frm.refresh_field('items');
//                         //                 frappe.msgprint(__('Items fetched successfully.'));
//                         //             }
//                         //         }
//                         //     });
//                         // }
//                 // //     },
//                 //     __('Get Items from Inquiry Form'),
//                 //     __('Fetch Items'));
//             }, __('Get Items From'));
//         }
//     }
// ); 


// frappe.ui.form.on('Request for Quotation', {
//     refresh(frm) {
//         frm.add_custom_button(__('Inquiry Form..'), () => {
//             new frappe.ui.form.MultiSelectDialog({
//                 doctype: 'Inquiry Form',
//                 target: frm,
//                 setters: {},
//                 get_query() {
//                     // exclude already-linked inquiries
//                     const existing = (frm.doc.items || [])
//                         .map(d => d.inquiry_reference)
//                         .filter(d => !!d);
//                     return {
//                         filters: [
//                             ['docstatus', 'in', [0, 1]],
//                             ['name', 'not in', existing] // hide already added ones
//                         ]
//                     };
//                 },
//                 action(selections) {
//                     if (selections && selections.length) {
//                         frm.call({
//                             method: "arabsat.doctype.request_for_quotation.request_for_quotation.get_inquiry_items",
//                             args: { 
//                                 inquiry_names: JSON.stringify(selections),
//                                 rfq_name: frm.doc.name
//                             },
//                             callback(r) {
//                                 if (r.message) {
//                                     (r.message || []).forEach(i => {
//                                         let row = frm.add_child('items');
//                                         Object.assign(row, i);
//                                     });
//                                     frm.refresh_field('items');
//                                     frappe.msgprint(__('Items fetched successfully.'));
//                                 }
//                             }
//                         });
//                     }
//                     cur_dialog.hide();
//                 }
//             });
//         }, __('Get Items From'));
//     }
// });




// pere code.

// frappe.ui.form.on('Request for Quotation', {
//     refresh(frm) {
//         frm.add_custom_button(__('Inquiry Form..'), () => {
//             new frappe.ui.form.MultiSelectDialog({
//                 doctype: 'Inquiry Form',
//                 target: frm,
//                 setters: {},
//                 get_query() {
//                     // exclude already-linked inquiries from dialog
//                     const existing = (frm.doc.items || [])
//                         .map(d => d.inquiry_reference)
//                         .filter(Boolean); // removes null/undefined

//                     return {
//                         filters: [
//                             ['docstatus', 'in', [0, 1]],
//                             ['name', 'not in', existing.length ? existing : ['']]
//                         ]
//                     };
//                 },
//                 action(selections) {
//                     if (selections && selections.length) {
//                         // Pass rfq_name safely (ignore new unsaved form name)
//                         const rfq_name = frm.doc.name && !frm.doc.name.startsWith("new-") 
//                             ? frm.doc.name 
//                             : null;

//                         frm.call({
//                             method: "arabsat.doctype.request_for_quotation.request_for_quotation.get_inquiry_items",
//                             args: { 
//                                 inquiry_names: JSON.stringify(selections),
//                                 rfq_name: rfq_name
//                             },
//                             freeze: true,
//                             freeze_message: __("Fetching items..."),
//                             callback(r) {
//                                 if (r.message && r.message.length) {
//                                     let added = 0;
//                                     (r.message || []).forEach(i => {
//                                         // Skip if already exists (safety)
//                                         const already = (frm.doc.items || []).some(
//                                             row => row.item_code === i.item_code && row.inquiry_reference === i.inquiry_reference
//                                         );
//                                         if (!already) {
//                                             const row = frm.add_child('items');
//                                             Object.assign(row, i);
//                                             added++;
//                                         }
//                                     });
//                                     frm.refresh_field('items');
//                                     frappe.msgprint(__('{0} item(s) fetched successfully.', [added]));
//                                 } else {
//                                     frappe.msgprint(__('No new items found.'));
//                                 }
//                             }
//                         });
//                     }
//                     cur_dialog.hide();
//                 }
//             });
//         }, __('Get Items From'));
//     }
// });

////////////////////////////////31-10-2025
// frappe.ui.form.on('Request for Quotation', {
//     refresh(frm) {
//         frm.add_custom_button(__('Inquiry Form..'), () => {

//             const company_filter = frm.doc.company
//                 ? ['company', '=', frm.doc.company]
//                 : null;

//             new frappe.ui.form.MultiSelectDialog({
//                 doctype: 'Inquiry Form',
//                 target: frm,
//                 setters: {},
//                 get_query() {
//                     // exclude already-linked inquiries from dialog
//                     const existing = (frm.doc.items || [])
//                         .map(d => d.inquiry_reference)
//                         .filter(Boolean); // removes null/undefined

//                     return {
//                         filters: [
//                             ['docstatus', 'in', [0, 1]],
//                             ['name', 'not in', existing.length ? existing : ['']]
//                         ]
//                     };
//                 },
//                 action(selections) {
//                     if (selections && selections.length) {
//                         // Pass rfq_name safely (ignore new unsaved form name)
//                         const rfq_name = frm.doc.name && !frm.doc.name.startsWith("new-") 
//                             ? frm.doc.name 
//                             : null;

//                         frm.call({
//                             method: "arabsat.doctype.request_for_quotation.request_for_quotation.get_inquiry_items",
//                             args: { 
//                                 inquiry_names: JSON.stringify(selections),
//                                 rfq_name: rfq_name
//                             },
//                             freeze: true,
//                             freeze_message: __("Fetching items..."),
//                             callback(r) {
//                                 if (r.message && r.message.length) {
//                                     let added = 0;
//                                     (r.message || []).forEach(i => {
//                                         // Skip if already exists (safety)
//                                         const already = (frm.doc.items || []).some(
//                                             row => row.item_code === i.item_code && row.inquiry_reference === i.inquiry_reference
//                                         );
//                                         if (!already) {
//                                             const row = frm.add_child('items');
//                                             Object.assign(row, i);
//                                             added++;
//                                         }
//                                     });
//                                     frm.refresh_field('items');
//                                     frappe.msgprint(__('{0} item(s) fetched successfully.', [added]));
//                                 } else {
//                                     frappe.msgprint(__('No new items found.'));
//                                 }
//                             }
//                         });
//                     }
//                     cur_dialog.hide();
//                 }
//             });
//         }, __('Get Items From'));
//     }
// });

frappe.ui.form.on('Request for Quotation', {
    refresh(frm) {
        frm.add_custom_button(__('Inquiry Form..'), () => {

            // ✅ Make sure Company is selected or show all
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

                    // ✅ Add company filter only if company selected
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
