{
    'name': 'excel_pipeline',
    'version': '16.0.0.1',
    'category': 'accounting',
    'summary': 'ecommerse internal machinery',
    'description': """
This module contains all the common features of Sales Management and eCommerce.
    """,
    'depends': ['crm', 'report_xlsx'],
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'wizard/pipeline_wizard.xml',
        'report/pipeline_report.xml',

    ]

}