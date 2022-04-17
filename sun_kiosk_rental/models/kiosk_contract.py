from odoo import fields, models


class KioskContract(models.Model):
    _name = 'kiosk.contract'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Kiosk Contract"
    
    name = fields.Char(string='Name', required=True, tracking=True)
    partner_id = fields.Many2one('res.partner', string='Customer', required=True, tracking=True)
    kiosk_id = fields.Many2one('kiosk.kiosk', string='Kiosk', required=True)
    representer_id = fields.Many2one('res.users', string='Representer')
    amount = fields.Float(string='Amount/Month')
    contract_duration = fields.Integer(string='Contract Duration', reuquired=True, tracking=True)
    state = fields.Selection([('draft', 'Draft'),
                              ('opened', 'Opened'),
                              ('closed', 'Closed')], string='State', default='draft', tracking=True)
    cost_type_ids = fields.One2many('contract.cost.type', 'kiosk_contract_id', string='List Cost Type', tracking=True)
    start_date = fields.Date(string='Start Date', default=fields.Date.today, tracking=True)
    end_date = fields.Date(string='End Date', default=fields.Date.today, tracking=True)
    
    def action_open(self):
        self.write({'state': 'opened'})
        
    def action_close(self):
        self.write({'state': 'closed'})
    
    def action_draft(self):
        self.write({'draft': 'draft'})
