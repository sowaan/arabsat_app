


import frappe
import json

@frappe.whitelist()
def get_inquiry_items(inquiry_names):
    """
    Fetch items from single or multiple Inquiry Form documents
    and return them to add in RFQ Items table.
    """

    # Convert string input to list if needed
    if isinstance(inquiry_names, str):
        inquiry_names = json.loads(inquiry_names)

    items = []

    # Get global default warehouse
    default_warehouse = frappe.db.get_single_value("Stock Settings", "default_warehouse")

    if not default_warehouse:
        frappe.throw("Please set a Default Warehouse in Stock Settings.")

    # Loop through all selected inquiries
    for inquiry_name in inquiry_names:
        inquiry = frappe.get_doc("Inquiry Form", inquiry_name)

        # Loop through each child row in the inquiry table
        for d in inquiry.table_fiwe:
            # Use warehouse from child table if available, otherwise default
            warehouse = getattr(d, "warehouse", None) or default_warehouse

            items.append({
                "item_code": d.item,
                "item_name": d.item_name,
                "description": d.description,
                "uom": d.uom,
                "conversion_factor": 1,
                "qty": d.quantity,
                "warehouse": warehouse,             # warehouse added
                "inquiry_reference": inquiry.name   # link back to inquiry
            })

    return items
