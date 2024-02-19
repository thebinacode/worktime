from django.db import models
import uuid
import os


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/logos', filename)


class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_joined = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(Department, related_name='employees', on_delete=models.SET_NULL, null=True)
    profile_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Attendance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    work_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)
    employee = models.ForeignKey(Employee, related_name='attendances', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.work_date} {self.start_time} {self.end_time}"
