# -*- coding: utf-8 -*-
from openerp import models, fields, api

class FaReservationExamination(models.Model):
    _name = 'fa_reservation_examination'

    reservation_id = fields.Integer('reservation_id', required = True)
    examination_id = fields.Integer('examination_id', required = True)
