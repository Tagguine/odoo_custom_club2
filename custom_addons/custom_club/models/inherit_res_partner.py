from odoo.odoo import models, fields, api


class InheritResPartner(models.Model):
    _inherit = 'res.partner'

    club_or = fields.Boolean(string="Club Or", dafault=False, Required=False)
