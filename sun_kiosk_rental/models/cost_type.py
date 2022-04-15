from odoo import fields, models


class CostType(models.Model):
    _name = 'cost.type'
    _description = "Cost Type"
    
    name = fields.Char(string='Name', required=True)
    type = fields.Selection([('water', 'Water'),
                             ('electric', 'Electric'),
                             ('other', 'Other')], default='other', string='Type', required=True)
    price = fields.Float(string='Unit Price')
    description = fields.Text(string='Description')
