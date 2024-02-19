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
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.CharField(write_only=True)

    class Meta:
        model = models.Employee
        fields = '__all__'

    def save(self, **kwargs):
        department = models.Department.objects.get(id=self.validated_data['department_id'])
        return super().save(department=department, **kwargs)


class EmployeeDetailSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    attendances = AttendanceSerializer(read_only=True, many=True)

    class Meta:
        model = models.Employee
        fields = '__all__'
