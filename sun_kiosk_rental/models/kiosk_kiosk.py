from odoo import fields, models, api


class KioskKiosk(models.Model):
    _name = 'kiosk.kiosk'
    _description = "Kiosk"
    
    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
    amount = fields.Float(string='Amount/Month')
    water_number_ids = fields.One2many('kiosk.water.number', 'kiosk_id', string='List Water Numbers')
    electric_number_ids = fields.One2many('kiosk.electric.number', 'kiosk_id', string='List Electric Numbers')
    electric_number_count = fields.Integer(string='Electric Number Count', compute='_compute_electric_number_count', store=True)
    water_number_count = fields.Integer(string='Water Number Count', compute='_compute_water_number_count')
    
    @api.depends('electric_number_ids')
    def _compute_electric_number_count(self):
        for r in self:
            r.electric_number_count = len(r.electric_number_ids)
            
    @api.depends('electric_number_ids')
    def _compute_water_number_count(self):
        for r in self:
            r.water_number_count = len(r.water_number_ids)
    
    def action_view_kiosk_electric_number(self):
        self.ensure_one()
        action = self.env['ir.actions.act_window']._for_xml_id('sun_kiosk_rental.kiosk_electric_number_action')
        electric_numbers = self.electric_number_ids
        action['context'] = {'default_kiosk_id': self.id}
        action['domain'] = [('id', 'in', electric_numbers.ids)]
        return action
    
    def action_view_kiosk_water_number(self):
        self.ensure_one()
        action = self.env['ir.actions.act_window']._for_xml_id('sun_kiosk_rental.kiosk_water_number_action')
        water_numbers = self.water_number_ids
        action['context'] = {'default_kiosk_id': self.id}
        action['domain'] = [('id', 'in', water_numbers.ids)]
        return action
