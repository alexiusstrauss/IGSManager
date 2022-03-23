from http import HTTPStatus

from django.test import TestCase
from employee.models import Departament


class TestApi(TestCase):

    def _fake_departament(self):
        payload = {
            "description": "derpartamento de teste"
        }

        return Departament.objects.get_or_create(**payload)[0]

    def test_departament_status_code(self):
        response = self.client.get('/api/departament/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_create_departament_w_status_code(self):
        response = self.client.post('/api/departament/', {'description': 'derpartamento de teste'})
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.json()['description'], 'derpartamento de teste')

    def test_create_departament_w_invalid_payload(self):
        response = self.client.post('/api/departament/', {'blabla': 'blabla'})
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_delete_departament_w_status_code(self):
        fake_departament = self._fake_departament()
        response = self.client.delete(f'/api/departament/{fake_departament.id}/')
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)

    def test_employee_status_code(self):
        response = self.client.get('/api/employee/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_create_employee_w_status_code(self):
        payload = {
            "name": "Employee Test",
            "email": "blabla@gmail.com",
            "departament": self._fake_departament().id
        }

        response = self.client.post('/api/employee/', payload)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

    def test_delete_employee_w_status_code(self):
        payload = {
            "name": "Employee Test",
            "email": "blabla@gmail.com",
            "departament": self._fake_departament().id
        }

        response = self.client.post('/api/employee/', payload)
        response = self.client.delete(f'/api/employee/{response.json()["id"]}/')
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)
