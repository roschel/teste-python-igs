from rest_framework.test import APITestCase
from .models import Employee
from departments.models import Department


class TestEmployees(APITestCase):
    url = '/api/v1/employees'

    def setUp(self):
        department = Department.objects.create(name="department_test")
        Employee.objects.create(name="John Doe", email="john@email.com", department=department)

    def test_get_employees(self):
        response = self.client.get(f"{self.url}/", headers={"Content-Type": "application/json"})
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]["name"], "John Doe")

    def test_get_employee_by_id(self):
        response = self.client.get(f"{self.url}/1/", headers={"Content-Type": "application/json"})
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["name"], "John Doe")
