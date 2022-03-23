from rest_framework import serializers
from employee.models import Employee, Departament


class DepartamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departament
        fields = ('id', 'description', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at',)


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'name', 'email', 'departament',
                  'created_at', 'updated_at',)

        read_only_fields = ('id', 'created_at', 'updated_at',)
