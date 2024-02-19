from rest_framework import serializers
from employee import models


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Attendance
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = models.Employee
        fields = '__all__'


class EmployeeDetailSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    attendances = AttendanceSerializer(read_only=True, many=True)

    class Meta:
        model = models.Employee
        fields = '__all__'
