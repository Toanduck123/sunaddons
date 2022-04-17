from odoo import fields, models, api


class KioskElectricNumber(models.Model):
    _name = 'kiosk.electric.number'
    _description = "Kiosk Electric Number"
    _order = 'date desc'

    name = fields.Char(string='Name', required=True)
    user_id = fields.Many2one('res.users', string='Employee', default=lambda self: self.env.user, required=True)
    kiosk_id = fields.Many2one('kiosk.kiosk', string='Kiosk', required=True)
    date = fields.Date(string='Date', default=fields.Date.today, required=True)
    number = fields.Integer(string='Number on Clock', required=True)
    
    @api.onchange('kiosk_id')
    def _onchange_kiosk_id(self):
        if self.kiosk_id:
            self.name = self.kiosk_id.name
