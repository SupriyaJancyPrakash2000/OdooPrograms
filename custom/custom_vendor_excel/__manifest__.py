{
    "name": "vendor_excel_report",
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
    "depends": ["base", "sale","purchase","report_xlsx","account"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/vendor_wizard.xml",
        "report/report_vendor.xml",
        "views/vendor_wizard_menu.xml",
        
       
    ],
}
