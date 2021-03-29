#!/usr/bin/python3
"""Test suit"""
import unittest
import pep8

class test_console(unittest.TestCase):
    """unittest class for console"""

    def test_pep8(self):
        """method for test pep8 on console.py"""
        pep8check = pep8.StyleGuide(quiet=True)
        check = pep8check.check_files(['console.py'])
        self.assertEqual(check.total_errors, 0, "style error go fix it."