# -*- coding: utf-8 -*-
from openerp import models, fields, api

class FaReservation(models.Model):
    _name = 'fa.reservation'

    # name                 = fields.Char('name', required=True)
    # age                  = fields.Integer('age')
    # gender               = fields.Selection([('male', "男"), ('female', '女')], string='gender')
    # mobile_phone         = fields.Char('mobile_phone')
    # location             = fields.Char('location')

    id_card_num          = fields.Char('id_card_num')
    aasm_state           = fields.Selection(selection=[
                                             ('to_prepay', ' 待支付定金'), ('prepaid', '匹配中'), ('to_examine',  '待检查'),
                                             ('to_consult',  '待咨询'), ('consulting',  '咨询中'), ('to_pay', '待支付'), ('paid',  '已支付'),
                                             ('diagnosed',  '医生服务已完成'), ('cancelled',  '已取消'),
                                             ('overdued',  '超时未支付定金'), ('rated',  '已评价')
                                             ], string='state', default='pending')

    # 用户想预约在什么时候
    p_date               = fields.Datetime('p_date')
    # 用户预约的时候所在位置
    p_location           = fields.Char('p_location')
    # reservation_type     = fields.Selection(selection=[('offline', 'offline'), ('online', 'online')], string='reservation_type')
    # 用户预约的时候填的手机号
    p_phone              = fields.Char('p_phone')

    # 医生确定好的预约时间，地点
    d_date               = fields.Datetime('d_date')
    d_location           = fields.Datetime('d_location')

    out_trade_prepay_no  = fields.Char('out_trade_prepay_no')
    out_trade_pay_no     = fields.Char('out_trade_pay_no')

    prepay_fee           = fields.Integer(string='prepay_fee', default=0)
    pay_fee              = fields.Integer(string='pay_fee', default=0)
    total_fee            = fields.Integer(string='total_fee', default=0)

    chief_complains      = fields.Char('chief_complains')
    reservation_name     = fields.Char('reservation_name')
    reservation_remark   = fields.Char('reservation_remark')

    user_id              = fields.Integer(string="预约人")
    doctor_id            = fields.Integer(string="医生")
    assistant_id         = fields.Integer(string="助手")
    family_member_id     = fields.Integer(string="小孩")

    height               = fields.Integer(string="身高")
    weight               = fields.Integer(string="体重")

    can_be_arranged      = fields.Boolean(string="是否接受调配")


    created_at           = fields.Datetime('created_at')
    updated_at           = fields.Datetime('updated_at')


    # active = fields.Boolean('Active?', default=True)

    # @api.one
    # def do_toggle_done(self):
    #   self.is_done = not self.is_done
    #   return True
    #
    # @api.multi
    # def do_clear_done(self):
    #   done_recs = self.search([('is_done', '=', True)])
    #   done_recs.write({'active': False})
    #   return True
