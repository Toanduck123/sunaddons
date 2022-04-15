from odoo import fields, models


class KioskKiosk(models.Model):
    _name = 'kiosk.kiosk'
    _description = "Kiosk"
    
    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
    image = fields.Binary(string='Photo', attachment=True)
    amount = fields.Float(string='Amount/Month')
    water_number_ids = fields.One2many('kiosk.water.number', 'kiosk_id', string='List Water Numbers')
    electric_number_ids = fields.One2many('kiosk.electric.number', 'kiosk_id', string='List Electric Numbers')
    electric_number_count = fields.Integer(string='Electric Number Count')
    water_number_count = fields.Integer(string='Water Number Count')
    def action_view_kiosk_electric_number(self):
        pass 
    
    def action_view_kiosk_water_number(self):
        pass
