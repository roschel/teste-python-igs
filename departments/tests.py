from rest_framework.test import APITestCase

from departments.models import Department


class TestDepartments(APITestCase):
    url = '/api/v1/departments'

    def setUp(self):
        Department.objects.create(name="department_test")

    def test_get_departments(self):
        response = self.client.get(f"{self.url}/", headers={"Content-Type": "application/json"})
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]["name"], "department_test")

    def test_get_department_by_id(self):
        response = self.client.get(f"{self.url}/1/", headers={"Content-Type": "application/json"})
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["name"], "department_test")
