# Generated by Django 5.0.2 on 2024-02-19 19:34

import employee.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=employee.models.get_file_path),
        ),
    ]
