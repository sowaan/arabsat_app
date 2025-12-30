import frappe

def sync_opportunity_items(doc, method=None):
    if not doc.opportunity:
        return

    opp = frappe.get_doc("Opportunity", doc.opportunity)

    # Optional: prevent submitted Opportunity update
    if opp.docstatus == 1:
        return

    inquiry_map = {
        row.item: row
        for row in doc.table_fiwe
        if row.item
    }

    updated = False

    for opp_item in opp.items:
        src = inquiry_map.get(opp_item.item_code)
        if not src:
            continue

        if opp_item.qty != src.quantity or opp_item.rate != src.rate:
            opp_item.qty = src.quantity
            opp_item.rate = src.rate
            opp_item.amount = (src.quantity or 0) * (src.rate or 0)
            updated = True

    if updated:
        opp.flags.ignore_permissions = True
        opp.save()
