import unittest
from daily.server import Api


class ServerTest(unittest.TestCase):
    def setUp(self):
        self.api = Api()

    def test_login(self):
        username = 'test'
        password = 'test'
        result = self.api.login(username, password)
        self.assertIsNotNone(result)
