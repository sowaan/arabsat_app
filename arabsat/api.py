# # import frappe
# # from frappe.utils import nowdate
# # from frappe.model.mapper import get_mapped_doc

# # @frappe.whitelist()
# # def create_inquiry_from_opportunity(opportunity):
# #     """
# #     Create an Inquiry Form from an Opportunity
# #     Copies key fields and items from Opportunity and Opportunity Item.
# #     """

# #     def set_missing_values(source, target):
# #         # Fill in any custom or additional fields after mapping
# #         target.opportunity = source.name
# #         target.company = source.company
# #         target.customer_name = source.customer_name
# #         target.contact_email = source.contact_email
# #         target.contact_person = source.contact_person
# #         target.opportunity_type = source.opportunity_type

# #         # ✅ FIX: Auto-fill RFQ Date
# #         if not target.rfq_date:
# #             target.rfq_date = nowdate()

# #     # Create Inquiry Form by mapping from Opportunity
# #     doc = get_mapped_doc(
# #         "Opportunity",
# #         opportunity,
# #         {
# #             "Opportunity": {
# #                 "doctype": "Inquiry Form",
# #                 "field_map": {
# #                     "name": "opportunity",
# #                     "company": "company",
# #                     "customer_name": "customer_name",
# #                     "contact_email": "contact_email",
# #                     "contact_person": "contact_person",
# #                     "opportunity_type": "opportunity_type",
# #                 },
# #             },
# #             "Opportunity Item": {
# #                 "doctype": "Inquiry Items",
# #                 "field_map": {
# #                     "item_code": "item",
# #                     "item_name": "item_name",
# #                     "qty": "quantity",
# #                     "uom": "uom",
# #                     "description": "description",
# #                 },
# #             },
# #         },
# #         target_doc=None,
# #         postprocess=set_missing_values,
# #     )

# #     # Save the new Inquiry Form document
# #     doc.insert(ignore_permissions=True)
# #     frappe.db.commit()

# #     return doc








# import frappe
# from frappe.utils import nowdate
# from frappe.model.mapper import get_mapped_doc

# @frappe.whitelist()
# def create_inquiry_from_opportunity(opportunity):
#     """
#     Create an Inquiry Form from an Opportunity
#     Copies key fields and items from Opportunity and Opportunity Item.
#     """

#     def set_missing_values(source, target):
#         # Copy key values
#         target.opportunity = source.name
#         target.company = source.company
#         target.customer_name = source.customer_name
#         target.contact_email = source.contact_email
#         target.contact_person = source.contact_person
#         target.opportunity_type = source.opportunity_type

       
#         if not target.rfq_date:
#             target.rfq_date = nowdate()

#     # Map Opportunity → Inquiry Form + Items
#     doc = get_mapped_doc(
#         "Opportunity",
#         opportunity,
#         {
#             "Opportunity": {
#                 "doctype": "Inquiry Form",
#                 "field_map": {
#                     "name": "opportunity",
#                     "company": "company",
#                     "customer_name": "customer_name",
#                     "contact_email": "contact_email",
#                     "contact_person": "contact_person",
#                     "opportunity_type": "opportunity_type",
#                 },
#             },
#             "Opportunity Item": {
#                 "doctype": "Inquiry Items",
#                 "field_map": {
#                     "item_code": "item",
#                     "item_name": "item_name",
#                     "qty": "quantity",
#                     "uom": "uom",
#                     "description": "description",
#                 },
#             },
#         },
#         target_doc=None,
#         postprocess=set_missing_values,
#     )

#     # Return new document (don't insert here)
#     return doc




import frappe
from frappe.utils import nowdate
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def create_inquiry_from_opportunity(opportunity):
    """
    Create an Inquiry Form from an Opportunity
    Copies key fields (Name, Mobile, Email ID) and Items.
    """

    def set_missing_values(source, target):

        # Basic linking
        target.opportunity = source.name
        target.company = source.company

        target.opportunity_reference = source.name

        # Customer details mapping
        target.name = source.customer_name or ""
        target.mobile = source.contact_mobile or ""
        target.email_id = source.contact_email or ""

        target.contact_person = source.contact_person
        target.opportunity_type = source.opportunity_type

        if not target.rfq_date:
            target.rfq_date = nowdate()

    # Map Opportunity → Inquiry Form + Items
    doc = get_mapped_doc(
        "Opportunity",
        opportunity,
        {
            "Opportunity": {
                "doctype": "Inquiry Form",
                "field_map": {
                    "name": "opportunity",
                    "company": "company",
                    "customer_name": "name1",
                    "contact_mobile": "mobile",
                    "contact_email": "email_id",
                    "contact_person": "contact_person",
                    "opportunity_type": "opportunity_type",
                },
            },
            "Opportunity Item": {
                "doctype": "Inquiry Items",
                "field_map": {
                    "item_code": "item",
                    "item_name": "item_name",
                    "qty": "quantity",
                    "uom": "uom",
                    "description": "description",
                 

                },
            },
        },
        target_doc=None,
        postprocess=set_missing_values,
    )

    
    # doc.insert(ignore_permissions=True)
    # frappe.db.commit()
    # doc.insert(ignore_permissions=True, ignore_mandatory=True)
    # frappe.db.commit()
    doc.set("__islocal", 1)
    doc.name = None

    
    # frappe.msgprint(f"Inquiry Form <b>{doc.name}</b> created successfully!")


    return doc




# import frappe
# from frappe.utils import nowdate
# from frappe.model.mapper import get_mapped_doc

# @frappe.whitelist()
# def create_inquiry_from_opportunity(opportunity):
#     """
#     Create an Inquiry Form from an Opportunity
#     Copies key fields (Name, Mobile, Email ID) and Items.
#     If source is not Customer, leaves fields blank safely.
#     """

#     def set_missing_values(source, target):
#         # Basic linking
#         target.opportunity = source.name  # e.g. CRM-OPP-2025-00015
#         target.company = source.company

#         # ✅ If from Customer → copy details
#         if source.opportunity_from == "Customer":
#             target.name = source.customer_name or ""
#             target.mobile = source.contact_mobile or ""
#             target.email_id = source.contact_email or ""
#         else:
#             # ✅ For Lead or Prospect → leave blank safely
#             target.name = ""
#             target.mobile = ""
#             target.email_id = ""

#         target.contact_person = source.contact_person or ""
#         target.opportunity_type = source.opportunity_type or ""

#         # ✅ Auto RFQ date
#         if not target.rfq_date:
#             target.rfq_date = nowdate()

#         # ✅ Reference field (read-only)
#         target.opportunity_reference = source.name

#     # Map Opportunity → Inquiry Form + Items
#     doc = get_mapped_doc(
#         "Opportunity",
#         opportunity,
#         {
#             "Opportunity": {
#                 "doctype": "Inquiry Form",
#                 "field_map": {
#                     "name": "opportunity",
#                     "company": "company",
#                     "customer_name": "name1",
#                     "contact_mobile": "mobile",
#                     "contact_email": "email_id",
#                     "contact_person": "contact_person",
#                     "opportunity_type": "opportunity_type",
#                 },
#             },
#             "Opportunity Item": {
#                 "doctype": "Inquiry Items",
#                 "field_map": {
#                     "item_code": "item",
#                     "item_name": "item_name",
#                     "qty": "quantity",
#                     "uom": "uom",
#                     "description": "description",
#                 },
#             },
#         },
#         target_doc=None,
#         postprocess=set_missing_values,
#     )

#     # ✅ Ignore mandatory field validation (since we control blank fields)
#     doc.insert(ignore_permissions=True, ignore_mandatory=True)
#     frappe.db.commit()

#     frappe.msgprint(f"Inquiry Form <b>{doc.name}</b> created successfully!")
#     return doc


# import frappe
# from frappe.utils import nowdate
# from frappe.model.mapper import get_mapped_doc

# @frappe.whitelist()
# def create_inquiry_from_opportunity(opportunity):
#     source = frappe.get_doc("Opportunity", opportunity)

#     # ✅ Check if linked record exists
#     if source.party_name and source.opportunity_from:
#         if not frappe.db.exists(source.opportunity_from, source.party_name):
#             frappe.throw(
#                 f"Could not find {source.opportunity_from}: {source.party_name}. "
#                 "Please ensure it exists or select a valid one in Opportunity."
#             )

#     def set_missing_values(source, target):
#         target.opportunity = source.name
#         target.company = source.company
#         target.contact_person = source.contact_person or ""
#         target.opportunity_type = source.opportunity_type or ""
#         target.rfq_date = target.rfq_date or nowdate()

#         # Fill customer/lead/prospect details
#         if source.opportunity_from == "Customer":
#             target.name = source.customer_name or ""
#             target.mobile = source.contact_mobile or ""
#             target.email_id = source.contact_email or ""
#         elif source.opportunity_from == "Prospect":
#             target.name = source.party_name or ""
#         elif source.opportunity_from == "Lead":
#             target.name = source.party_name or ""
#         else:
#             target.name = ""

#     # Map Opportunity → Inquiry Form
#     doc = get_mapped_doc(
#         "Opportunity",
#         opportunity,
#         {
#             "Opportunity": {
#                 "doctype": "Inquiry Form",
#                 "field_map": {
#                     "name": "opportunity",
#                     "company": "company",
#                     "customer_name": "name1",
#                     "contact_mobile": "mobile",
#                     "contact_email": "email_id",
#                     "contact_person": "contact_person",
#                     "opportunity_type": "opportunity_type",
#                 },
#             },
#             "Opportunity Item": {
#                 "doctype": "Inquiry Items",
#                 "field_map": {
#                     "item_code": "item",
#                     "item_name": "item_name",
#                     "qty": "quantity",
#                     "uom": "uom",
#                     "description": "description",
#                 },
#             },
#         },
#         target_doc=None,
#         postprocess=set_missing_values,
#     )

#     doc.insert(ignore_permissions=True, ignore_mandatory=True)
#     frappe.db.commit()
#     frappe.msgprint(f"Inquiry Form <b>{doc.name}</b> created successfully!")
#     return doc




#///////////////////////////////////////////////

# import frappe
# from frappe.utils import nowdate
# from frappe.model.mapper import get_mapped_doc

# @frappe.whitelist()
# def create_inquiry_from_opportunity(opportunity):
#     source = frappe.get_doc("Opportunity", opportunity)

#     # ✅ If linked record doesn't exist → auto-create it
#     if source.party_name and source.opportunity_from:
#         if not frappe.db.exists(source.opportunity_from, source.party_name):
#             # Automatically create the missing record
#             new_doc = frappe.new_doc(source.opportunity_from)
#             if source.opportunity_from == "Customer":
#                 new_doc.customer_name = source.party_name
#             elif source.opportunity_from == "Prospect":
#                 new_doc.prospect_name = source.party_name
#             elif source.opportunity_from == "Lead":
#                 new_doc.lead_name = source.party_name
#             new_doc.insert(ignore_permissions=True)
#             frappe.db.commit()
#             frappe.msgprint(
#                 f"Auto-created {source.opportunity_from} <b>{source.party_name}</b> because it did not exist."
#             )

#     # ✅ Mapping Opportunity → Inquiry Form
#     def set_missing_values(source, target):
#         target.opportunity = source.name
#         target.company = source.company
#         target.contact_person = source.contact_person or ""
#         target.opportunity_type = source.opportunity_type or ""
#         target.rfq_date = target.rfq_date or nowdate()

#         # Fill party details safely
#         target.name = source.party_name or ""
#         target.mobile = source.contact_mobile or ""
#         target.email_id = source.contact_email or ""

#     doc = get_mapped_doc(
#         "Opportunity",
#         opportunity,
#         {
#             "Opportunity": {
#                 "doctype": "Inquiry Form",
#                 "field_map": {
#                     "name": "opportunity",
#                     "company": "company",
#                     "customer_name": "name1",
#                     "contact_mobile": "mobile",
#                     "contact_email": "email_id",
#                     "contact_person": "contact_person",
#                     "opportunity_type": "opportunity_type",
#                 },
#             },
#             "Opportunity Item": {
#                 "doctype": "Inquiry Items",
#                 "field_map": {
#                     "item_code": "item",
#                     "item_name": "item_name",
#                     "qty": "quantity",
#                     "uom": "uom",
#                     "description": "description",
#                 },
#             },
#         },
#         target_doc=None,
#         postprocess=set_missing_values,
#     )

#     # ✅ Save Inquiry Form (ignore mandatory if needed)
#     doc.insert(ignore_permissions=True, ignore_mandatory=True)
#     frappe.db.commit()

#     frappe.msgprint(f"Inquiry Form <b>{doc.name}</b> created successfully!")
#     return doc
