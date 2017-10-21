# -*- coding: utf-8 -*-
from openerp import models, fields, api

class FaDoctor(models.Model):
    _name = 'fa.doctor'

    name                   = fields.Char('name', required = True)
    gender                 = fields.Selection([('1', "男"), ('0', '女')], string='gender')
    avatar                 = fields.Char('avatar')
    age                    = fields.Integer('age')
    date_of_birth          = fields.Datetime('date_of_birth')
    latitude               = fields.Float('lat')
    longtitude             = fields.Float('long')
    verified               = fields.Boolean(string='verified?', default=False)
    mobile_phone           = fields.Char('mobile_phone')
    user_id                = fields.Many2one('user_id')

    id_card_num            = fields.Char('id_card_num')
    id_card_front          = fields.Binary('id_card_front')
    id_card_back           = fields.Binary('id_card_back')
    id_card_front_media_id = fields.Char('id_card_front_media_id')
    id_card_back_media_id  = fields.Char('id_card_back_media_id')
    license_front_media_id = fields.Char('license_front_media_id')
    license_back_media_id  = fields.Char('license_back_media_id')
    license_front          = fields.Binary('license_front')
    license_back           = fields.Binary('license_back')

    remark                 = fields.Char('remark')
    hospital               = fields.Char('hospital')
    job_title              = fields.Char('job_title')
    work_address           = fields.Char('work_address')
    home_address           = fields.Char('home_address')
    good_at                = fields.Char('good_at')
    created_at             = fields.Datetime('created_at')
    updated_at             = fields.Datetime('updated_at')

    @api.one
    def verify(self):
        self.verified = True
        return True




class FaWallet(models.Model):
    _name = 'fa.wallet'

    user_id = fields.Many2one('user_id')
    balance_withdrawable = fields.Float('balance_withdrawable', default=0.0)
    balance_unwithdrawable = fields.Float('balance_unwithdrawable', default=0.0)
    balance_withdrawable = fields.Float('balance_withdrawable')
    created_at           = fields.Datetime('created_at')
    updated_at           = fields.Datetime('updated_at')




class Transaction(models.Model):
    _name = 'fa.transaction'
    reservation_id = fields.Many2one('reservation_id')
    amount = fields.Float('amount', default=0.0)
    source = fields.Char('source')
    withdraw_target = fields.Char('withdraw_target')
    operation = fields.Char('operation')
    user_id = fields.Many2one('user_id')
    aasm_state    = fields.Selection(selection=[ ('pending', '待定'), ('settled', '已完成')
                                        ], string='state', default='pending')
    created_at           = fields.Datetime('created_at')
    updated_at           = fields.Datetime('updated_at')
