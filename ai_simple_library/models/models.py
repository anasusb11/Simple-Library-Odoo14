from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    
    penulis = fields.Boolean(string= 'Penulis ?')
    anggota = fields.Boolean(string='Anggota ?')
    penerbit = fields.Boolean(string= 'Penerbit ?')
    
    born_date = fields.Date(string='Date Of Birth')
    death_date = fields.Date(string='Date Of Death')
    
    biography = fields.Text(string='Biography')
    # lang = fields.Selection(string='Language', selection='_get_lang')
    
    
    _sql_constraints = [('name_uniq', 'unique(name)', 'Namanya Harus Unik!')]
    
    # @api.model
    # def _get_lang(self):
    #     return self.env['res.lang'].get.installed()
    
