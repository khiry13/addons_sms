from odoo import models, fields


class ItemSelection(models.TransientModel):
    _name = 'sms_module.item_selection'
    _description = 'Temporary Item Selection'

    name = fields.Char(string="Item Name", required=True)


