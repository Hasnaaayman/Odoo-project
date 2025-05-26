from odoo import models, fields, api
from odoo.exceptions import UserError

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    github_account = fields.Char(string="GitHub Account")
    collaborator_project_ids = fields.One2many('project.collaborator', 'employee_id', string="Projects")

    def write(self, vals):
        if 'active' in vals and not vals['active']:
            for employee in self:
                active_collaborations = employee.collaborator_project_ids.filtered(lambda c: c.status == 'active')
                if active_collaborations:
                    raise UserError("Cannot archive employee while active in project(s).")
        return super().write(vals)
