# coding: utf-8

"""
    Codex API

    List of endpoints and interfaces available to Codex API users

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from codex_client.models.sales_availability_create import SalesAvailabilityCREATE

class TestSalesAvailabilityCREATE(unittest.TestCase):
    """SalesAvailabilityCREATE unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SalesAvailabilityCREATE:
        """Test SalesAvailabilityCREATE
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SalesAvailabilityCREATE`
        """
        model = SalesAvailabilityCREATE()
        if include_optional:
            return SalesAvailabilityCREATE(
                id = '0x...',
                total_size = '',
                duration = '',
                min_price = '',
                max_collateral = ''
            )
        else:
            return SalesAvailabilityCREATE(
                total_size = '',
                duration = '',
                min_price = '',
                max_collateral = '',
        )
        """

    def testSalesAvailabilityCREATE(self):
        """Test SalesAvailabilityCREATE"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
