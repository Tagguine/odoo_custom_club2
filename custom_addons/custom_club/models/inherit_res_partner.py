from odoo import api, fields, models


# Question 1 - 4
class InheritResPartner(models.Model):
    _inherit = 'res.partner'

    club_or = fields.Boolean(string='Club Or', default=False, required=False)
