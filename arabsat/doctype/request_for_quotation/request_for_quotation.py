


# import frappe
# import json

# @frappe.whitelist()
# def get_inquiry_items(inquiry_names):
#     """
#     Fetch items from single or multiple Inquiry Form documents
#     and return them to add in RFQ Items table.
#     """

#     # Convert string input to list if needed
#     if isinstance(inquiry_names, str):
#         inquiry_names = json.loads(inquiry_names)

#     items = []

#     # Get global default warehouse
#     default_warehouse = frappe.db.get_single_value("Stock Settings", "default_warehouse")

#     if not default_warehouse:
#         frappe.throw("Please set a Default Warehouse in Stock Settings.")

#     # Loop through all selected inquiries
#     for inquiry_name in inquiry_names:
#         inquiry = frappe.get_doc("Inquiry Form", inquiry_name)

#         # Loop through each child row in the inquiry table
#         for d in inquiry.table_fiwe:
#             # Use warehouse from child table if available, otherwise default
#             warehouse = getattr(d, "warehouse", None) or default_warehouse

#             items.append({
#                 "item_code": d.item,
#                 "item_name": d.item_name,
#                 "description": d.description,
#                 "uom": d.uom,
#                 "conversion_factor": 1,
#                 "qty": d.quantity,
#                 "warehouse": warehouse,             # warehouse added
#                 "inquiry_reference": inquiry.name   # link back to inquiry
#             })

    # return items

# import frappe
# import json

# @frappe.whitelist()
# def get_inquiry_items(inquiry_names, rfq_name=None):
#     """
#     Fetch items from Inquiry Form(s), skip already-added inquiries for this RFQ,
#     and remove duplicate items within same fetch.
#     """

#     if isinstance(inquiry_names, str):
#         inquiry_names = json.loads(inquiry_names)

#     items = []
#     seen_keys = set()

#     # --- Get Default Warehouse ---
#     default_warehouse = frappe.db.get_single_value("Stock Settings", "default_warehouse")
#     if not default_warehouse:
#         frappe.throw("Please set a Default Warehouse in Stock Settings.")

#     # --- Get already-linked inquiries ---
#     existing_inquiries = set()
#     if rfq_name:
#         rfq_doc = frappe.get_doc("Request for Quotation", rfq_name)
#         for row in rfq_doc.items:
#             if row.get("inquiry_reference"):
#                 existing_inquiries.add(row.inquiry_reference)

#     # --- Fetch new inquiries only ---
#     for inquiry_name in inquiry_names:
#         if inquiry_name in existing_inquiries:
#             frappe.msgprint(f"Inquiry {inquiry_name} is already linked with this RFQ. Skipping.")
#             continue

#         inquiry = frappe.get_doc("Inquiry Form", inquiry_name)
#         for d in inquiry.table_fiwe:
#             warehouse = getattr(d, "warehouse", None) or default_warehouse
#             key = (d.item, warehouse)

#             if key not in seen_keys:
#                 seen_keys.add(key)
#                 items.append({
#                     "item_code": d.item,
#                     "item_name": d.item_name,
#                     "description": d.description,
#                     "uom": d.uom,
#                     "conversion_factor": 1,
#                     "qty": d.quantity,
#                     "warehouse": warehouse,
#                     "inquiry_reference": inquiry.name
#                 })

#     return items
# pre code.
# import frappe
# import json

# @frappe.whitelist()
# def get_inquiry_items(inquiry_names, rfq_name=None):
#     """
#     Fetch items from Inquiry Form(s), skip already-added inquiries for this RFQ,
#     and remove duplicate items within same fetch.
#     """

#     # --- Parse inquiry names safely ---
#     if isinstance(inquiry_names, str):
#         try:
#             inquiry_names = json.loads(inquiry_names)
#         except Exception:
#             inquiry_names = [x.strip() for x in inquiry_names.split(",") if x.strip()]

#     items = []
#     seen_keys = set()

#     # --- Get Default Warehouse ---
#     default_warehouse = frappe.db.get_single_value("Stock Settings", "default_warehouse")
#     if not default_warehouse:
#         frappe.throw("Please set a Default Warehouse in Stock Settings.")

#     # --- Get existing linked inquiries (only if RFQ already saved) ---
#     existing_inquiries = set()
#     if rfq_name and not rfq_name.startswith("new-"):
#         try:
#             rfq_doc = frappe.get_doc("Request for Quotation", rfq_name)
#             for row in rfq_doc.items:
#                 if row.get("inquiry_reference"):
#                     existing_inquiries.add(row.inquiry_reference)
#         except frappe.DoesNotExistError:
#             pass  # safe to ignore if doc not found (unsaved RFQ)

#     # --- Fetch Inquiry Items ---
#     for inquiry_name in inquiry_names:
#         if inquiry_name in existing_inquiries:
#             frappe.msgprint(f"⚠ Inquiry <b>{inquiry_name}</b> is already linked with this RFQ. Skipping.")
#             continue

#         inquiry = frappe.get_doc("Inquiry Form", inquiry_name)
#         for d in inquiry.table_fiwe:
#             warehouse = getattr(d, "warehouse", None) or default_warehouse
#             key = (d.item, warehouse)

#             if key not in seen_keys:
#                 seen_keys.add(key)
#                 items.append({
#                     "item_code": d.item,
#                     "item_name": d.item_name,
#                     "description": d.description,
#                     "uom": d.uom,
#                     "conversion_factor": 1,
#                     "qty": d.quantity,
#                     "warehouse": warehouse,
#                     "inquiry_reference": inquiry.name
#                 })

#     return items
# /////////////////////////////////////////////////try 31-10-2025


# /////////
# import frappe
# import json

# @frappe.whitelist()
# def get_inquiry_items(inquiry_names, rfq_name=None):
#     """
#     Fetch items from Inquiry Form(s), skip already-added inquiries for this RFQ,
#     and remove duplicate items within same fetch.
#     """

#     # --- Parse inquiry names safely ---
#     if isinstance(inquiry_names, str):
#         try:
#             inquiry_names = json.loads(inquiry_names)
#         except Exception:
#             inquiry_names = [x.strip() for x in inquiry_names.split(",") if x.strip()]

#     items = []
#     seen_keys = set()

#     # --- Get Default Warehouse ---
#     default_warehouse = frappe.db.get_single_value("Stock Settings", "default_warehouse")
#     if not default_warehouse:
#         frappe.throw("Please set a Default Warehouse in Stock Settings.")

#     # --- Get existing linked inquiries (only if RFQ already saved) ---
#     existing_inquiries = set()
#     if rfq_name and not rfq_name.startswith("new-"):
#         try:
#             rfq_doc = frappe.get_doc("Request for Quotation", rfq_name)
#             for row in rfq_doc.items:
#                 if row.get("inquiry_reference"):
#                     existing_inquiries.add(row.inquiry_reference)
#         except frappe.DoesNotExistError:
#             pass  # safe to ignore if doc not found (unsaved RFQ)

#     # --- Fetch Inquiry Items ---
#     for inquiry_name in inquiry_names:
#         if inquiry_name in existing_inquiries:
#             frappe.msgprint(f"⚠ Inquiry <b>{inquiry_name}</b> is already linked with this RFQ. Skipping.")
#             continue

#         inquiry = frappe.get_doc("Inquiry Form", inquiry_name)
          
#         # # ✅ Company check
#         # if rfq_name:
#         #     rfq_company = frappe.db.get_value("Request for Quotation", rfq_name, "company")
#         #     if inquiry.company != rfq_company:
#         #         frappe.throw(f"Inquiry {inquiry_name} belongs to company {inquiry.company}, "
#         #                      f"but this RFQ is for company {rfq_company}.")
                
#         for d in inquiry.table_fiwe:
#             warehouse = getattr(d, "warehouse", None) or default_warehouse
#             key = (d.item, warehouse)

#             if key not in seen_keys:
#                 seen_keys.add(key)
#                 items.append({
#                     "item_code": d.item,
#                     "item_name": d.item_name,
#                     "description": d.description,
#                     "uom": d.uom,
#                     "conversion_factor": 1,
#                     "qty": d.quantity,
#                     "warehouse": warehouse,
#                     "inquiry_reference": inquiry.name
#                 })

#     return items

import frappe
import json

@frappe.whitelist()
def get_inquiry_items(inquiry_names, rfq_name=None):
    """
     Fetch items from multiple Inquiry Forms.
    - Adds all selected inquiry items to RFQ.
    - Skips inquiries already linked with the RFQ.
    - Avoids duplicate items per inquiry.
    """

    # --- Parse inquiry names safely ---
    if isinstance(inquiry_names, str):
        try:
            inquiry_names = json.loads(inquiry_names)
        except Exception:
            inquiry_names = [x.strip() for x in inquiry_names.split(",") if x.strip()]

    if not isinstance(inquiry_names, (list, tuple)):
        inquiry_names = [inquiry_names]

    frappe.msgprint(f"Fetching items from {len(inquiry_names)} inquiry form(s)...")

    items = []
    seen_keys = set()

    # --- Get Default Warehouse ---
    default_warehouse = frappe.db.get_single_value("Stock Settings", "default_warehouse")
    if not default_warehouse:
        frappe.throw("Please set a Default Warehouse in Stock Settings.")

    # --- Get existing linked inquiries (only if RFQ already saved) ---
    existing_inquiries = set()
    if rfq_name and not rfq_name.startswith("new-"):
        try:
            rfq_doc = frappe.get_doc("Request for Quotation", rfq_name)
            for row in rfq_doc.items:
                if row.get("inquiry_reference"):
                    existing_inquiries.add(row.inquiry_reference)
        except frappe.DoesNotExistError:
            pass  # safe to ignore if doc not found (unsaved RFQ)

    # --- Fetch Inquiry Items ---
    for inquiry_name in inquiry_names:
        if inquiry_name in existing_inquiries:
            frappe.msgprint(f"⚠ Inquiry <b>{inquiry_name}</b> is already linked with this RFQ. Skipping.")
            continue

        inquiry = frappe.get_doc("Inquiry Form", inquiry_name)

        for d in inquiry.table_fiwe:
            warehouse = getattr(d, "warehouse", None) or default_warehouse

            # Unique key per item per inquiry
            key = (d.item, warehouse, inquiry.name)
            if key not in seen_keys:
                seen_keys.add(key)
                items.append({
                    "item_code": d.item,
                    "item_name": d.item_name,
                    "description": d.description,
                    "uom": d.uom,
                    "conversion_factor": 1,
                    "qty": d.quantity,
                    "warehouse": warehouse,
                    "inquiry_reference": inquiry.name
                })

    frappe.msgprint(f"✅ Total items collected: {len(items)}")
    return items
