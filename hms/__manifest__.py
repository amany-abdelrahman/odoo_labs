{
    'name': "HMS",
    'summary': """ """,
    'description': """Hoapital Management System""",
    'author': "Amany Abdelrahman",
    'category': "Productivity",
    'version': '17.0.0.1.0',
    'depends': ['base'],
    'application': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        'views/department_views.xml',
        'views/doctor_views.xml',

    ]
}