#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

 
class transaction(models.Model):
    _name = 'ridwan_library.transaction'
    _description = 'ridwan_library.transaction'

    name = fields.Char('Name', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    loan_date = fields.Date('Loan Date')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('progress', 'In Progress'),
        ('done', 'Done')
    ], string='State', default='draft')
    return_date = fields.Date('Return Date')
    book_id = fields.Many2one('ridwan_library.book', string='Book')
    description = fields.Text('Description')
    partner_id = fields.Many2one('res.partner', 'Customer')


    @api.model
    def create(self, vals):
        seq_date = None
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('ridwan_library.transaction') or _('New')
        result = super(transaction, self).create(vals)
        return result

    def action_confirm(self):
        if self.book_id.available_book > 0:
            self.state = 'progress'
            self.return_date = fields.Date.today()
            self.book_id.count_transaction()
        else:
            raise ValidationError("Stok Buku {} Sedang Tidak Tersedia".format(self.book_id.name))

    def action_done(self):
        self.state = 'done'
        self.return_date = fields.Date.today()
        self.book_id.count_transaction()

    def action_set_draft(self):
        self.state = 'draft'
        self.book_id.count_transaction()