# Generated by Django 4.2.2 on 2023-06-22 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarkAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100)),
                ('mark_time', models.TimeField()),
                ('shift', models.CharField(max_length=100)),
            ],
        ),
    ]
