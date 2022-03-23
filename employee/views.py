from rest_framework import generics

from employee.models import Departament, Employee
from employee.serializers import DepartamentSerializer, EmployeeSerializer


class DepartamentListCreate(generics.ListCreateAPIView):
    queryset = Departament.objects.all()
    serializer_class = DepartamentSerializer


class DepartamentRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departament.objects.all()
    serializer_class = DepartamentSerializer


class EmployeetListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
