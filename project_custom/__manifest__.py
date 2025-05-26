{
    'name': 'Project Custom Enhancements',
    'version': '1.0',
    'depends': ['project', 'hr'],
    'author': 'Your Company',
    'category': 'Project',
    'description': 'Enhancements to Project module to track Odoo-specific fields and collaborators.',
    'data': [
        'security/ir.model.access.csv',
        'views/project_project_views.xml',
        'views/project_collaborator_views.xml',
    ],
    'installable': True,
    'application': False,
}