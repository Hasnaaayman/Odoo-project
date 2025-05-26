from odoo import models,fields

class ProjectCollaborator(models.Model):
    _name = 'project.collaborator'
    _description = 'Project Collaborator'

    project_id = fields.Many2one('project.project', string="Project", required=True, ondelete='cascade')
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], default='inactive', string="Status")

    def set_active(self):
        for record in self:
            record.status = 'active'

    def set_inactive(self):
        for record in self:
            record.status = 'inactive'