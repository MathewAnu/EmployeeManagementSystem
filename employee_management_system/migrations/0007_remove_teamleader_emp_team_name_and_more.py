# Generated by Django 4.0.4 on 2022-04-23 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management_system', '0006_remove_teamleader_emp_team_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamleader',
            name='emp_team_name',
        ),
        migrations.AddField(
            model_name='teamleader',
            name='emp_team_name',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s', to='employee_management_system.team'),
        ),
    ]
