from odoo import fields, models, api


class KioskPaymentLine(models.Model):
    _name = 'kiosk.payment.line'
    _description = "Kiosk Payment Line"
    
    name = fields.Char(string='Name', required=True)
    kiosk_payment_id = fields.Many2one('kiosk.payment', string='Kiosk Payment', required=True, ondelete='cascade')
    cost_type_id = fields.Many2one('cost.type', string='Cost Type', required=True)
    quantity = fields.Integer(string='Quantity', required=True)
    price = fields.Float(string='Unit Price', required=True)
    sub_amount_total = fields.Float(string='Amount Total', compute='_compute_sub_amount_total', store=True)
    
    @api.depends('quantity', 'price')
    def _compute_sub_amount_total(self):
        for r in self:
            r.sub_amount_total = r.quantity * r.price
    
    @api.onchange('cost_type_id')
    def _onchange_cost_type_id(self):
        if self.cost_type_id:
            self.name = self.cost_type_id.name