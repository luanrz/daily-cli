import unittest
from daily.config import CustomConfig


class ConfigTest(unittest.TestCase):
    def setUp(self):
        self.config = CustomConfig()

    def test_set(self):
        custom_server_url = 'http://localhost:8080'
        self.config.set('server_url', custom_server_url)
        server_url = self.config.get('server_url')
        self.assertEqual(server_url, custom_server_url)

    def test_get(self):
        server_url = self.config.get('server_url')
        self.assertIsNotNone(server_url)

    def test_delete(self):
        key = 'test'
        self.config.set(key, 'test')
        self.config.delete(key)
        value = self.config.get(key)
        self.assertIsNone(value)

    def test_list(self):
        config_dict = self.config.list()
        self.assertIsNotNone(config_dict['server_url'])
