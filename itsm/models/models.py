# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class c:\users\it\documents\odoo(models.Model):
#     _name = 'c:\users\it\documents\odoo.c:\users\it\documents\odoo'
#     _description = 'c:\users\it\documents\odoo.c:\users\it\documents\odoo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
