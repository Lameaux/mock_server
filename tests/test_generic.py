import json

from tests.test_base import BaseTestCase, API_HEADERS


class GenericTestCase(BaseTestCase):
    def test_generic_with_default_params(self):
        response = self.client.get('/generic', headers=API_HEADERS)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['status_code'], 200)
        self.assertEqual(json_response['sleep_seconds'], 0)

    def test_generic_with_params(self):
        response = self.client.get('/generic?status_code=300&sleep_seconds=1', headers=API_HEADERS)
        self.assertEqual(response.status_code, 300)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['status_code'], 300)
        self.assertEqual(json_response['sleep_seconds'], 1)