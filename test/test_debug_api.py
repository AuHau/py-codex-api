# coding: utf-8

"""
    Codex API

    List of endpoints and interfaces available to Codex API users

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from codex_client.api.debug_api import DebugApi


class TestDebugApi(unittest.TestCase):
    """DebugApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DebugApi()

    def tearDown(self) -> None:
        pass

    def test_get_debug_info(self) -> None:
        """Test case for get_debug_info

        Gets node information
        """
        pass

    def test_set_debug_log_level(self) -> None:
        """Test case for set_debug_log_level

        Set log level at run time
        """
        pass


if __name__ == '__main__':
    unittest.main()
