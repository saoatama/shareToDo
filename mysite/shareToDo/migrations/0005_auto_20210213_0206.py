# Generated by Django 3.1.6 on 2021-02-13 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareToDo', '0004_auto_20210213_0203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='participant',
            name='role',
            field=models.IntegerField(default=1),
        ),
    ]