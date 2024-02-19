from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, \
    RetrieveUpdateAPIView

from employee import serializers
from employee import models


class EmployeeListCreateAPIView(ListCreateAPIView):
    serializer_class = serializers.EmployeeSerializer
    queryset = models.Employee.objects.all()


class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.EmployeeDetailSerializer
    queryset = models.Employee.objects.all()


class AttendanceListCreateAPIView(ListCreateAPIView):
    serializer_class = serializers.AttendanceSerializer
    queryset = models.Attendance.objects.all()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.employee_id = None

    def dispatch(self, request, *args, **kwargs):
        self.employee_id = kwargs['pk']
        return super().dispatch(request, *args, **kwargs)

    def perform_create(self, serializer):
        employee = models.Employee.objects.get(id=self.employee_id)
        serializer.save(employee=employee)

    def get_queryset(self):
        return models.Attendance.objects.filter(employee__id=self.employee_id)


class AttendanceUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = serializers.AttendanceSerializer
    queryset = models.Attendance.objects.all()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.employee_id = None

    def dispatch(self, request, *args, **kwargs):
        self.employee_id = kwargs['employee_id']
        return super().dispatch(request, *args, **kwargs)

    def perform_update(self, serializer):
        employee = models.Employee.objects.get(id=self.employee_id)
        serializer.save(employee=employee)


class DepartmentListCreateAPIView(ListCreateAPIView):
    serializer_class = serializers.DepartmentSerializer
    queryset = models.Department.objects.all()


class DepartmentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.DepartmentSerializer
    queryset = models.Department.objects.all()
