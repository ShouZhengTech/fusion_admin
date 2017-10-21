# -*- coding: utf-8 -*-
from openerp import models, fields, api

class FaPatient(models.Model):
    _name = 'fa.patient'

    name = fields.Char('name', required = True)
    age = fields.Integer('age')
    gender   = fields.Selection([('male', "男"), ('female', '女')], string='gender')
    id_card_num = fields.Char('id_card_num')
    date_of_birth = fields.Datetime('date_of_birth')
    blood_type = fields.Selection([('A', "A"), ('B', 'B'),('O', 'O'),('AB','AB')], string='blood type')
