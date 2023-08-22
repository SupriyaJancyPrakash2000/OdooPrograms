{
    "name": "excel_report",
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
    "depends": ["base", "sale","purchase","report_xlsx"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/wizard_excel.xml",
        "views/wizard_menu.xml",
        "report/sale_xlsx.xml",
        "security/security_group_xlsx.xml"
       
    ],
}
