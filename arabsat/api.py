
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

    doc.set("__islocal", 1)
    doc.name = None

    return doc