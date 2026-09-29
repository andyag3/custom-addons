# -*- coding: utf-8 -*-
##############################################################################
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
##############################################################################

import json

import requests

from ..exceptions.exceptions import ErrorGettingToken, InvalidCredentials, InvalidToken, UnregisteredError

TOKEN_BEARER = "/auth/requestToken"
REGISTER_PAYMENT = "/invoice/registerPayment"
TRADING_LICENSES = "/GetSpecifiedMachineryAndTradingLicences"
CUSTOMERS = "/applicant/customerProfileSearch"
APPLICATION_PROPERTY = "/minerProfile/mineralPropertySearch"
LIMIT = 14000
TIMEOUT = 3000


class ApiGgmc():

    def __init__(self, base_url):
        self.base_url = base_url

    def process_response(self, response):
        """Process Response Given From ApiGgmc

        :param response: Received response
        :type response: requests.models.Response
        :raises InvalidCredentials: When credentials are not valid
        :raises UnregisteredError: When the error is unexpected
        :return: Response body
        :rtype: dict
        """
        # Try to decode the response as JSON, but handle non-JSON responses
        try:
            data = response.json()
        except ValueError:
            # If it's not JSON, assign the text content to `data`
            data = response.text

        # Handle 401 (Unauthorized)
        if response.status_code == 401:
            raise InvalidToken('The provided token is invalid')

        # Handle 500 (Internal Server Error)
        if response.status_code == 500:
            raise UnregisteredError(f'Internal server error occurred. Response: {data}')

        # Handle other non-200 status codes
        if response.status_code != 200:
            raise UnregisteredError(f'Unregistered error querying API: {data}')

        return data

    def get_token_bearer(self, username, password, timeout=TIMEOUT):
        """Method to get a token from the ApiGgmc endpoint

        :param username: Connection username
        :type username: str
        :param password: Connection password
        :type password: str
        :param timeout: Optional timeout for request, defaults to TIMEOUT
        :type timeout: int, optional
        :return: Token returned from ApiGgmc
        :rtype: str
        """
        url = self.base_url + TOKEN_BEARER
        credentials = {
            "username": username,
            "password": password
        }
        response = requests.post(url, json=credentials, timeout=timeout)
        if response.status_code == 401:
            raise InvalidCredentials('The provided credentials are invalid')
        if response.status_code != 200:
            raise ErrorGettingToken('Unidentified error getting token')
        return response.json().get('token')

    def notify_payment_post(self, jwt_token, payment, timeout=TIMEOUT):
        """Payment notification

        :param jwt_token: Authentication token required for  ApiGgmc endpoint
        :type jwt_token: str
        :param payment: Payment details to notify
        :type payment: dict
        :return: Response from ApiGgmc
        :rtype: dict
        """
        url = self.base_url + REGISTER_PAYMENT
        headers = {
            'Content-Type': 'application/json',
            "Authorization": f"Bearer {jwt_token}"
        }
        response = requests.post(url, headers=headers, data=json.dumps(payment), timeout=timeout)
        return self.process_response(response)

    def get_machinery_trading_licenses(self, jwt_token,
        status_date=None, input_param=None, limit=LIMIT, timeout=TIMEOUT):
        """Get valid specified machinery and trading licences in [{}, {}, ...] format

        :param jwt_token: Authentication token required for endpoint
        :type jwt_token: str
        :param status_date: Optional date to filter licenses
        (format: 'YYYY-MM-DD'), defaults to None
        :type status_date: date, optional
        :param input_param: Optional input parameter for filtering, defaults to None
        :type input_param: str, optional
        :param limit: Optional limit for the number of records, defaults to LIMIT
        :type limit: int, optional
        :param timeout: Optional timeout for request, defaults to TIMEOUT
        :type timeout: int, optional
        :return: Response from GGMC
        :rtype: list(dict)
        """
        url = self.base_url + TRADING_LICENSES
        headers = {
            'Content-Type': 'application/json',
            "Authorization": f"Bearer {jwt_token}"
        }

        # Building the query parameters
        params = {}
        if status_date:
            params['statusDate'] = status_date.strftime('%Y-%m-%d')
        if input_param:
            params['input'] = input_param
        if limit:
            params['limit'] = limit

        response = requests.get(url, headers=headers, params=params, timeout=timeout)
        return self.process_response(response)

    def get_customer(self, jwt_token, id_search=None,
        last_updated=None, limit=LIMIT, timeout=TIMEOUT):
        """Get customers in [{}, {}, ...] format

        :param jwt_token: Authentication token required for endpoint
        :type jwt_token: str
        :param id_search: Optional param for search by id, defaults to None
        :type id_search: str, optional
        :param last_updated: Optional date to filter customers, defaults to None
        :type last_updated: date, optional
        :param limit: Optional limit for the number of records, defaults to LIMIT
        :type limit: int, optional
        :param timeout: Optional timeout for request, defaults to TIMEOUT
        :type timeout: int, optional
        :return: Response from GGMC
        :rtype: list(dict)
        """
        url = self.base_url + CUSTOMERS
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }
        params = {}
        if id_search:
            params['idSearch'] = id_search
        if last_updated:
            params['lastUpdated'] = last_updated
        if limit:
            params['limit'] = limit
        response = requests.get(url, headers=headers, params=params, timeout=timeout)
        return self.process_response(response)

    def get_application_property(self, jwt_token, application_date=None,
        granted_date=None, last_updated= None, limit=LIMIT, timeout=TIMEOUT):
        """Get applications and properties in [{}, {}, ...] format

        :param application_date: Optional date to filter applications, defaults to None
        :type application_date: date, optional
        :param granted_date: Optional date to filter properties, defaults to None
        :type granted_date: date, optional
        :param last_updated: Optional date to filter applications and properties, defaults to None
        :type last_updated: date, optional
        :param limit: Optional limit for the number of records, defaults to LIMIT
        :type limit: int, optional
        :param timeout: Optional timeout for request, defaults to TIMEOUT
        :type timeout: int, optional
        :return: _Response from GGMC
        :rtype: list(dict)
        """
        url = self.base_url + APPLICATION_PROPERTY
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }
        params = {}
        if granted_date:
            params['grantedDate'] = granted_date
        if application_date:
            params['applicationDate'] = application_date
        if last_updated:
            params['lastUpdated'] = last_updated
        if limit:
            params['limit'] = limit
        response = requests.get(url, headers=headers, params=params, timeout=timeout)
        return self.process_response(response)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
