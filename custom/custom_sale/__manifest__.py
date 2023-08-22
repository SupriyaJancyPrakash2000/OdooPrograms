{
    "name": "custom_sale",
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
    "depends": ["base", "sale","purchase","account"],
    "data": [
        "Security/security_group_custom.xml",
        "views/sale_order.xml",
        "views/sale_order_notebook.xml",
        "views/user_sale.xml",
        "views/search_groupby.xml",
        "views/invoice_creation_check.xml",
        "views/check_confirm.xml"
       
    ],
}
