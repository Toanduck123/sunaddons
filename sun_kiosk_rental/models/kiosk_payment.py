from odoo import fields, models, api


class KioskPayment(models.Model):
    _name = 'kiosk.payment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Kiosk Payment"
    
    name = fields.Char(string='Name', required=True, tracking=True)
    kiosk_contract_id = fields.Many2one('kiosk.contract', string='Kiosk Contract', required=True, tracking=True)
    kiosk_id = fields.Many2one(related='kiosk_contract_id.kiosk_id')
    partner_id = fields.Many2one(related='kiosk_contract_id.partner_id')
    start_date = fields.Date(string='Start Date', default=fields.Date.today().replace(day=1), required=True, tracking=True)
    end_date = fields.Date(string='End Date', default=fields.Date.today, required=True, tracking=True)
    kiosk_payment_line_ids = fields.One2many('kiosk.payment.line', 'kiosk_payment_id', string='Payment Lines')
    amount_total = fields.Float(string='Amount Total', compute='_compute_amount_all', store=True)
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),
                              ('send_email', 'Send Email'),
                              ('paymented', 'Paymented'),
                              ], string='State', default='draft', require=True)
    
    note = fields.Text(string='Notes')
    
    @api.depends('kiosk_payment_line_ids',
                 'kiosk_payment_line_ids.sub_amount_total')
    def _compute_amount_all(self):
        for r in self:
            amount_total = sum(r.kiosk_payment_line_ids.mapped('sub_amount_total'))
            r.amount_total = amount_total
            
    @api.onchange('kiosk_contract_id')
    def _onchange_cost_type_id(self):
        if self.kiosk_contract_id:
            self.name = self.kiosk_contract_id.name
    
    def action_confirm(self):
        self.write({'state': 'confirmed'})
        
    def action_send_email(self):
        self.write({'state': 'send_email'})
        template_id = self.env.ref('sun_kiosk_rental.email_template_kiosk_payment_partner').id
        self._action_send_mail_common(template_id)
    
    def action_paymented(self):
        self.write({'state': 'paymented'})
    
    def action_draft(self):
        self.write({'state': 'draft'})
        
    def compute_payment(self):
        self.kiosk_payment_line_ids = [(5, 0, 0)]
        vals_list = []
        for rec in self:
            kiosk = rec.kiosk_id
            start_date = rec.start_date
            end_date = rec.end_date
            cost_types = rec.kiosk_contract_id.cost_type_ids
            for r in cost_types:
                vals=r._prepare_payment_line_vals(kiosk, start_date, end_date)
                vals.update({
                    'kiosk_payment_id': rec.id
                    })
                vals_list.append(vals)
        self._create_payment_line(vals_list)
            
    def _create_payment_line(self, vals_list):
        return self.env['kiosk.payment.line'].create(vals_list)
    
    def _action_send_mail_common(self, template_id):
        self.ensure_one()
        template = self.env['mail.template'].browse(template_id)
        # setting email
        self.message_post_with_template(template.id)
