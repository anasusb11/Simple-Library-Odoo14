# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ai_simple_library(models.Model):
#     _name = 'ai_simple_library.ai_simple_library'
#     _description = 'ai_simple_library.ai_simple_library'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
