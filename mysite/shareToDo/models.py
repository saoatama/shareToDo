from django.db import models

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=200)
    open_close = models.BooleanField(verbose_name='',default=False,)

class User(models.Model):
    user_name = models.CharField(max_length=200)
    est_date = models.DateTimeField('date published', null=True)
    user_room = models.ManyToManyField("Room", through="UserRoomRelation",)

class UserRoomRelation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)

class Category(models.Model):
    category_name = models.CharField(max_length=200)

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    deadline = models.DateTimeField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    role = models.IntegerField(default=1)

class Role(models.Model):
    role_name = models.CharField(max_length=200)
