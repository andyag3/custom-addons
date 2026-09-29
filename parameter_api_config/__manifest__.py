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
    "name": "Parameter Api config",
    "version": "19.0.1.0.0",
    "category": "",
    "summary": "Parameter for Api",
    "author": "BLUEORANGE GROUP S.R.L. (www.blueorange.com.ar) / NEXIT",
    "website": "https://www.nexit.com.uy",
    "license": "AGPL-3",
    "depends": ["base"],
    "data": [
        "data/ir_config_parameter.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": False,
    "description": """Parameter for Api:
        -URL
        -Token
        -User
        -Password
    And exceptins
    """,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
