from odoo import fields, models, api


class InheritSaleOrder(models.Model):
    _inherit = 'sale.order'

    club_or = fields.Boolean(string='Club Or', related='partner_id.club_or', default=False)
    possible_discount = fields.Float(string='Possible Discount ', required=False, compute='_compute_possible_discount')

    @api.depends('amount_total')
    def _compute_possible_discount(self):
        if self.club_or:
            self.possible_discount = self.amount_total * 0.1
        else:
            self.possible_discount = 0
