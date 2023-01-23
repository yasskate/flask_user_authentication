import unittest

from base_test import BaseTestCase
from src.accounts.forms import LoginForm, RegisterForm

class TestRegisterForm(BaseTestCase):
    def test_validate_success_register_form(self):
        form = RegisterForm(email="new@test.com", password="tset", confirm="example")
        self.assertTrue(form.validate())

    def test_validate_success_register_form(self):
        form = RegisterForm(email="new@test.com", password="tset", confirm="")
        self.assertFalse(form.validate())

    def test_validate_email_already_registered(self):
        form = RegisterForm(email="ad@min.com", password="admin_user", confirm="admin_user")
        self.assertFalse(form.validate())

class TestLoginForm(BaseTestCase):
    def test_validate_success_login_form(self):
        form = LoginForm(email="ad@min.com", password="admin_user")
        self.assertTrue(form.validate())

    def test_validate_invalid_email_format(self):
        form = LoginForm(email="unkown", password="example")
        self.assertFalse(form.validate())

if __name__ == "__main__":
    unittest.main()

