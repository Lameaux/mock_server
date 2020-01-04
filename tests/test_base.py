import unittest

from app import create_app

API_HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

