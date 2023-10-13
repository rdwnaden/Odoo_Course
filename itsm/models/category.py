# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Category(models.Model):
    _name = 'itsm.category'
    _description = 'Category'

    name = fields.Char(string='Name')
    
    