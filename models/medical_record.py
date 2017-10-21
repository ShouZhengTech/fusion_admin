# -*- coding: utf-8 -*-
from openerp import models, fields, api

class FaMedicalRecord(models.Model):
    _name = 'fa.medical_record'

    # fields.References('fa.patient')
    name = fields.Char('name')
    blood_type = fields.Selection([('A', "A"), ('B', 'B'),('O', 'O'),('AB','AB')], string='blood type')
    date_of_birth = fields.Datetime('date_of_birth')
    gender    = fields.Selection([('male', "男"), ('female', '女')], string='gender')
    onset_date = fields.Datetime('onset_date')
    chief_complaint = fields.Char("chief_complaint")
    history_of_present_illness = fields.Char("history_of_present_illness")
    past_medical_history = fields.Char("past_medical_history")
    allergic_history = fields.Char("allergic_history")
    personal_history = fields.Char("personal_history")
    family_history = fields.Char("family_history")
    vaccination_history = fields.Char("vaccination_history")
    physical_examination = fields.Char("physical_examination")
    laboratory_and_supplementary_examinations = fields.Char("laboratory_and_supplementary_examinations")
    preliminary_diagnosis = fields.Char("preliminary_diagnosis")
    treatment_recommendation = fields.Char("treatment_recommendation")
    remarks = fields.Char("remarks")
    imaging_examination = fields.Char("imaging_examination")
    height = fields.Integer('height')
    weight = fields.Float('weight')
    bmi = fields.Float('bmi')
    temperature = fields.Float('temperature')
    pulse = fields.Integer('pulse')
    respiratory_rate = fields.Integer('respiratory_rate')
    blood_pressure = fields.Integer('blood_pressure')
    oxygen_saturation = fields.Char('oxygen_saturation')
    pain_score = fields.Integer('pain_score')
    user_id = fields.Many2one('user_id')
    reservation_id = fields.Many2one('reservation_id')
    identity_card = fields.Char('identity_card')

    created_at = fields.Datetime('created_at')
    updated_at = fields.Datetime('updated_at')


class FaMedicalRecordImage(models.Model):
    _name = 'fa.medical_record_image'

    medical_record_id = fields.Many2one('medical_record_id')
    data = fields.Char('data')
    media_id = fields.Char('media_id')
    is_cover = fields.Boolean('is_cover')
    created_at = fields.Datetime('created_at')
    updated_at = fields.Datetime('updated_at')

class FaLaboratoryExaminationImage(models.Model):
    _name = 'fa.laboratory_examination_image'

    medical_record_id = fields.Many2one('medical_record_id')
    data = fields.Char('data')
    media_id = fields.Char('media_id')
    is_cover = fields.Boolean('is_cover')
    created_at = fields.Datetime('created_at')
    updated_at = fields.Datetime('updated_at')

class ImagingExaminationImage(models.Model):
    _name = 'fa.imaging_examination_image'

    medical_record_id = fields.Many2one('medical_record_id')
    data = fields.Char('data')
    media_id = fields.Char('media_id')
    is_cover = fields.Boolean('is_cover')
    created_at = fields.Datetime('created_at')
    updated_at = fields.Datetime('updated_at')
