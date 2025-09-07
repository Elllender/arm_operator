{
    'name': 'ARM Operator',
    'version': '1.0',
    'summary': 'Автоматизированное рабочее место оператора',
    'category': 'Manufacturing',
    'author': 'Pavel',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/arm_operator_task_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}
