{
    "name": "Recruitment",
    "summary": """
        hr""",
    "description": """
        Long description of module's purpose
    """,
    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Uncategorized",
    "version": "15.0.0.2",
    "depends": ["hr_recruitment","hr_payroll"],
    "data": [
        "security/ir.model.access.csv",
        "views/salary_sheet_connection.xml",
        "views/master_menu.xml",
        "views/company_rule.xml",
        "views/wage_field.xml",
        "report/paperformat.xml",
        "report/pdf_report_recruitment.xml"

    ],
}
