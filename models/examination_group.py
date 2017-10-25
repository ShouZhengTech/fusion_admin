# -*- coding: utf-8 -*-
from openerp import models, fields, api

class FaExaminationGroup(models.Model):
    _name = 'fa_examination_group'

    name = fields.Char('name', required = True)
