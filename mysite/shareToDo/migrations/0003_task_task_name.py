# Generated by Django 3.1.6 on 2021-02-13 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareToDo', '0002_remove_room_est_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_name',
            field=models.CharField(default='myTask', max_length=200),
            preserve_default=False,
        ),
    ]
