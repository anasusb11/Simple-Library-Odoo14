from odoo import models, fields, api



class ProductProduct(models.Model): 
    _inherit ='product.product'

    isbn = fields.Char('ISBN Code', help="Shows International Standard Book Number")
    catalog_num = fields.Char('Catalog Number', help="Shows Identification number of books")
    author_id = fields.Many2one('res.partner', 'Author')
    publisher_id = fields.Many2one('res.partner', 'Publisher')
    nbpage = fields.Integer('Number of Pages')
    location_id = fields.Many2one('stock.location', 'Location', help="Shows position of book")
    num_edition = fields.Integer('No. Edition', help="Edition number of book")
    resensi = fields.Text('Resensi')
    state = fields.Selection([('available', 'Available'), ('rent', 'Rented')], 'State', readonly=True, default='available')

    def action_rent(self):
        self.write ({'state' : 'rent'})

    def action_available(self):
        self.write ({'state' : 'available'})

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
    
    
