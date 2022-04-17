from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    kiosk_contract_ids = fields.One2many('kiosk.contract', 'partner_id', string='Contracts of Kiosk')
