from odoo import fields, models, api


class ContractCostType(models.Model):
    _name = 'contract.cost.type'
    _description = "Contract Cost Type"
    
    name = fields.Char(string='Name', required=True)
    kiosk_contract_id = fields.Many2one('kiosk.contract', string='Kiosk Contact', required=True, ondelete='cascade')
    cost_type_id = fields.Many2one('cost.type', string='Cost Type', required=True)
    value = fields.Float(string='Value', required=True)
    type = fields.Selection(related='cost_type_id.type', string='Type', store=True)
    
    @api.onchange('cost_type_id')
    def _onchange_cost_type_id(self):
        if self.cost_type_id:
            self.name = self.cost_type_id.name
            
    def _prepare_payment_line_vals(self, kiosk, start_date, end_date):
        self.ensure_one()
        quantity = self._compute_quantity(kiosk, start_date, end_date)
        vals = {
            'cost_type_id': self.cost_type_id.id,
            'name': self.name,
            'quantity': quantity,
            'price': self.value
            }
        return vals
    
    def _compute_quantity(self, kiosk, start_date, end_date):
        quantity = 0
        if self.type == 'water':
            water_numbers_from = kiosk.water_number_ids.filtered(lambda r: r.date < start_date)[:1]
            water_numbers_to = kiosk.water_number_ids.filtered(lambda r: r.date >= start_date and r.date <= end_date)[:1]
            if water_numbers_from and water_numbers_to:
                quantity += water_numbers_to.number - water_numbers_from.number
            elif not water_numbers_from and water_numbers_to:
                quantity += water_numbers_to.number
        elif self.type == 'electric':
            electric_numbers_from = kiosk.electric_number_ids.filtered(lambda r: r.date < start_date)[:1]
            electric_numbers_to = kiosk.electric_number_ids.filtered(lambda r: r.date >= start_date and r.date <= end_date)[:1]
            if electric_numbers_from and electric_numbers_to:
                quantity += electric_numbers_to.number - electric_numbers_from.number
            elif not electric_numbers_from and electric_numbers_to:
                quantity += electric_numbers_to.number
        else:
            quantity += 1
        return quantity
