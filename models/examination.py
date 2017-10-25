# -*- coding: utf-8 -*-
from openerp import models, fields, api

class FaExamination(models.Model):
    _name = 'fa_examination'

    name                      = fields.Char('name', required = True)
    examination_group_id      = fields.Integer(integer="检查")
