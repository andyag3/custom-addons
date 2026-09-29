# -*- coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{

    'name': 'Operating Unit Customization',

    'version': '19.0.1.0.0',

    'category': '',

    'summary': 'Operating Unit Customization',

    'author': 'BLUEORANGE GROUP S.R.L. (www.blueorange.com.ar) / NEXIT',

    'website': 'https://www.nexit.com.uy',

    'license': 'AGPL-3',

    'depends': [
        'operating_unit',
        'sale',
        'account',
        'product',

    ],

    'data': [
        'security/account_move_user.xml',
        'security/account_journal_user.xml',
        'security/analytic_account_user.xml',
        'security/product_user.xml',
        'security/sale_user.xml',
        'views/account_move_views.xml',
        'views/account_journal_views.xml',
        'views/analytic_account_views.xml',
        'views/product_views.xml',
        'views/sale_views.xml',

    ],

    'installable': True,

    'auto_install': False,

    'application': False,

    'description': """This module uses the separation by operational units to restrict users from viewing invoices, credit notes
                    sale orders, journals and products depending on their assigned operational units and the operational unit of the 
                    aforementioned documents.""",

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
