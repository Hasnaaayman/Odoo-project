from odoo import models, fields, api

class ProjectProject(models.Model):
    _inherit = 'project.project'

    odoo_version = fields.Integer(string='Odoo Version')
    odoo_types = fields.Selection([
        ('community', 'Community'),
        ('enterprise', 'Enterprise')
    ], default='enterprise', string="Odoo Type")
    github_repo_name = fields.Char(string="GitHub Repository Name")
    github_repo_url = fields.Char(string="GitHub Repository URL")
    hosting = fields.Selection([
        ('on_prem', 'On Prem'),
        ('cloud_hosting', 'Cloud Hosting'),
        ('odoo_sh', 'Odoo SH'),
        ('odoo_online', 'Odoo Online')
    ], string="Hosting")
    hosting_description = fields.Html(string="Hosting Description")

    collaborators_ids = fields.One2many('project.collaborator', 'project_id', string="Collaborators")