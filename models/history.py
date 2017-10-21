# -*- coding: utf-8 -*-
from openerp import models, fields, api

class FaPhoneCallHistory(models.Model):
    _name = 'fa.phone_call_history'

    # t.integer  "caller_user_id"
    # t.string   "caller_phone"
    # t.integer  "callee_user_id"
    # t.string   "callee_phone"
    # t.integer  "reservation_id"
    # t.string   "reservation_state_when_call"
    # t.datetime "created_at",                  null: false
    # t.datetime "updated_at",
class FaSmsHistory(models.Model):
    _name = 'fa.sms_history'

    # t.integer  "sender_user_id"
    # t.string   "sender_phone"
    # t.integer  "sendee_user_id"
    # t.string   "sendee_phone"
    # t.integer  "reservation_id"
    # t.string   "reservation_state_when_sms"
    # t.datetime "created_at",                 null: false
    # t.datetime "updated_at",                 null: false
    # t.integer  "template_id"
