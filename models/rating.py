# -*- coding: utf-8 -*-
from openerp import models, fields, api


class FaRating(models.Model):
    _name = 'fa.rating'

    stars                = fields.Float('stars')
    body                 = fields.Text('body')
    reservation_id       = fields.Integer('reservation_id')
    user_id              = fields.Integer('user_id')
    rated_by             = fields.Integer('rated_by')
    created_at           = fields.Datetime('created_at')
    updated_at           = fields.Datetime('updated_at')
