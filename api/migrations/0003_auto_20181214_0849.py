# Generated by Django 2.0 on 2018-12-14 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181214_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.CharField(choices=[('BL', 'Blocked'), ('OP', 'Open'), ('IP', 'In Progress'), ('IR', 'In Review'), ('CL', 'Closed')], default='OP', max_length=2),
        ),
    ]
