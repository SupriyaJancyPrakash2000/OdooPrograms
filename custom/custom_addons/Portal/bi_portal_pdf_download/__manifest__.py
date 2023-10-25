{
    'name': 'website form custom',
    'category': 'Hidden',
    'summary': 'website form custom',
    'version': '16.0.0.1',
    'description': """ """,
    'depends': ["portal","web","hr_timesheet"],
    'installable': True,
    'auto_install': True,
    'license': 'OEEL-1',
    "data": [
        "views/portal_custom.xml",
        "report/portal_form.xml",

    ],
    # 'assets':{
    #     'web.assets_frontend': [
    #                 'bi_portal_pdf_download/static/src/xml/portal_form.xml',
    #
    #     ]
    # }
}