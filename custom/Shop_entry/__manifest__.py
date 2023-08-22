{
    "name": "Shop_details",
    "summary": """
        Sale""",
    "description": """
        Long description of module's purpose
    """,
    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Uncategorized",
    "version": "15.0.0.2",
    "depends": ["base", "sale","purchase"],
    "data": [
        "Security/ir.model.access.csv",
        "Security/security_groups.xml",
        "wizard/wizard_view.xml",
        "views/sale_shop.xml",
        "views/accountmove.xml",
        "views/product_shop.xml",
        "views/shop_sequence.xml",
       
    ],
}
