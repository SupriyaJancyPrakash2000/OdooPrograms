{
    "name": "Notication Email Approve",
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
        "security/ir.model.access.csv",
        "views/notification_email_button.xml",
        "wizard/approve_salewizard.xml",
    ],
}
