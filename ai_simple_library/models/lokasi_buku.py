from odoo.exceptions import UserError
from odoo import models, fields, api

class StockLocation(models.Model):
    _inherit = 'stock.location'
 
    lokasi_buku = fields.Boolean(string='Lokasi Buku ?')