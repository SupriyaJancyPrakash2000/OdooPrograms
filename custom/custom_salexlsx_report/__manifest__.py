{
    "name": "sale_excel_report",
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
        "wizard/wizard_sale_xlsx.xml",
        "views/wizard_menu.xml",
        "report/xlsx_sale.xml"
        
       
    ],
}
