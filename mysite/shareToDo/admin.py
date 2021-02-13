from django.contrib import admin

from .models import Room, User, Task, Participant, Category, Role, UserRoomRelation

# Register your models here.
admin.site.register(Room)
admin.site.register(User)
admin.site.register(Task)
admin.site.register(Participant)
admin.site.register(Category)
admin.site.register(Role)
admin.site.register(UserRoomRelation)
