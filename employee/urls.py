from django.urls import path
from employee.views import api as api_views

urlpatterns = [
    path('', api_views.EmployeeListCreateAPIView.as_view()),
    path('<pk>/', api_views.EmployeeRetrieveUpdateDestroyAPIView.as_view()),
    path('<pk>/attendance/', api_views.AttendanceListCreateAPIView.as_view()),
    path('<employee_id>/attendance/<pk>/', api_views.AttendanceUpdateAPIView.as_view())
]
