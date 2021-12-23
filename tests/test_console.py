"""Test console"""
import unittest
import pycodestyle
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test the console"""

    @classmethod
    def setUpClass(self):
        """Class method called before tests in an individual class are run"""
        self.console = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """Class method called after tests in an individual class have run"""


    def testDocumentation(self):
        """Check documentation"""
        self.assertIsNotNone(self.console.__doc__)
        self.assertIsNotNone(HBNBCommand.__doc__)
        for method in dir(HBNBCommand):
            self.assertIsNotNone(method.__doc__)

    def test_pycodestyle(self):
        """Test pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
