from django.test import TestCase
from employee.models import Departament, Employee


class TestDeparamentModel(TestCase):

    def test_departament_create(self):
        payload = {
            "description": "Departamento de teste"
        }

        departament = Departament.objects.create(**payload)
        self.assertEqual(departament.description, payload.get('description'))
        self.assertEqual(departament.__str__(), payload.get('description'))

    def test_departament_delete(self):
        departament = Departament.objects.create(
            description='Departamento de teste'
        )
        departament.delete()
        self.assertEqual(Departament.objects.count(), 0)


class TestEmployeeModel(TestCase):

    def test_employee_create(self):

        departament = Departament.objects.create(
            description='Departamento de teste'
        )

        payload = {
            "name": "Employee Test",
            "email": "balbla@gmail.com",
            "departament": departament
        }

        employee = Employee.objects.create(**payload)
        self.assertEqual(employee.name, 'Employee Test')
        self.assertEqual(employee.departament.id, departament.id)
        self.assertEqual(employee.__str__(), payload.get('name'))
