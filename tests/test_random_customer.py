#!/usr/bin/env python

"""Tests for `random_customer` package."""

# import pytest
import unittest
from click.testing import CliRunner

from random_customer.random_customer import random_customer
from random_customer import cli


class TestRandomCustomer(unittest.TestCase, random_customer):
    """Tests for `pandas_utility` package."""

    # @pytest.fixture
    def setUp(self):
        """Set up test fixtures, if any."""
        self.new_customer = random_customer.CreateRandomCustomer(self)

    def test_create_random_customer(self):
        FirstName = self.new_customer['FirstName']
        LastName = self.new_customer['LastName']
        AddressLine1 = self.new_customer['AddressLine1']
        City = self.new_customer['City']
        StateCode = self.new_customer['StateCode']
        ZipCode = self.new_customer['Zip']
        PersonalEmail = self.new_customer['PersonalEmail']
        print(self.new_customer)
        self.assertNotEqual(FirstName, '', 'Could not generate First Name')
        self.assertNotEqual(LastName, '', 'Could not generate Last Name')
        self.assertNotEqual(AddressLine1, '', 'Could not generate Address Line 1')
        self.assertNotEqual(City, '', 'Could not generate City')
        self.assertNotEqual(StateCode, '', 'Could not generate State Code')
        self.assertNotEqual(ZipCode, '', 'Could not generate Zip Code')
        self.assertNotEqual(PersonalEmail, '', 'Could not generate Personal Email')

# def test_command_line_interface():
#     """Test the CLI."""
#     runner = CliRunner()
#     result = runner.invoke(cli.main)
#     assert result.exit_code == 0
#     assert 'random_customer.cli.main' in result.output
#     help_result = runner.invoke(cli.main, ['--help'])
#     assert help_result.exit_code == 0
#     assert '--help  Show this message and exit.' in help_result.output
