# -*- coding: utf-8 -*-
from openerp import models, fields, api

class FaReservationImage(models.Model):
    _name = 'fa_reservation_image'

    reservation_id = fields.Integer('reservation_id', required = True)
    data = fields.Char('data', required = True)
    media_id = fields.Char('media_id', required = True)
