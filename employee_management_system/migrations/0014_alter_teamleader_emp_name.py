# Generated by Django 4.0.4 on 2022-04-23 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management_system', '0013_workarrangement_work_time_percentange_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamleader',
            name='emp_name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
