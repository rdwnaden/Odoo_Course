#-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.http import request
import requests


class book(models.Model):
    _name = 'ridwan_library.book'
    _description = 'ridwan_library.book'

    name = fields.Char('Name')
    total = fields.Float('Total')
    description = fields.Text('Description')
    transaction_ids = fields.One2many('ridwan_library.transaction', inverse_name='book_id', string='Transcation')
    available_book = fields.Float(compute='count_transaction', string='Available Book')

    @api.depends('transaction_ids','total')
    def count_transaction(self):
        for rec in self:
            rec.available_book = rec.total - len(rec.transaction_ids.sudo().search([('state','=','progress')]))


    def act_generate_book(self):
        books = requests.get('https://simple-books-api.glitch.me/books').json()
        for book in books:
            vals = {
                'name' : book['name'],
                'description' : book['type'],
                'total' : book['id']
            }

            self.env['ridwan_library.book'].sudo().create(vals)

    _sql_constraints = [
                     ('name', 
                      'unique(name)',
                      'Choose another value - it has to be unique!')
    ]

