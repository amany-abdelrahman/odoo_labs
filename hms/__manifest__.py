{
    'name': "HMS",
    'summary': "Hospital Management System for managing patients, departments, and doctors.",
    'description': "Hospital Management System to efficiently manage hospital operations.",
    'author': "Amany Abdelrahman",
    'category': "Productivity",
    'version': '17.0.0.1.0',
    'depends': ['base'],
    'application': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/department_views.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/log_history.xml',
        'views/customer_views.xml',
    ]
}