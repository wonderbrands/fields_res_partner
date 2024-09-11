from odoo import models, fields, api, _

class ResPartnerRES(models.Model):
    _inherit = "res.partner"

    advance_payment_date = fields.Integer(string='Días de financiamiento', help='Cantidad de días de financiamiento')
    percent_supplier_advance = fields.Float(string='% Anticipo proveedor', help='Muestra el porcentaje de anticipo al proveedor')
    lt_ag_channel = fields.Integer(string='LT Producción', help='LT Producción')