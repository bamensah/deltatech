# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2015 Deltatech All Rights Reserved
#                    Dorin Hongu <dhongu(@)gmail(.)com       
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
##############################################################################

from openerp import models, fields, api, _
from openerp import SUPERUSER_ID
from openerp.addons.web.http import request
from openerp.tools.translate import _



class website(models.Model):
    _inherit = 'website'
 
    @api.multi
    def sale_product_domain(self):
        domain = super(website,self).sale_product_domain()
        search = request.params.get('search',False)
        if search:
            product_ids = []
            alt_domain = []
            for srch in search.split(" "):
                alt_domain += [ ('name', 'ilike', srch)]
            alternative_ids =  self.env['product.alternative'].search(  alt_domain, limit=10 ) 
            for alternative in alternative_ids:
                product_ids += alternative.product_tmpl_id.product_variant_ids.ids
            if product_ids:
                if len(product_ids)==1:
                    domain += ['|',('id','=', product_ids[0])]
                else:
                    domain += ['|',('id','in', product_ids)]
                print "cautare dupa:", domain           
        return domain



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
