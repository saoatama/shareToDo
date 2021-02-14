from django.urls import path

from . import views
app_name = 'shareToDo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.CategoryView.as_view(), name='detail'),
    path('post/', views.post, name='post'),
    path('room', views.RoomView.as_view(), name='room_create'),
    path('room_post', views.RoomView.room_post, name='room_post'),
    path('<int:pk>/room_modify', views.RoomModifyView.as_view(), name='room_modify'),
    path('room_modify_post', views.RoomModifyView.room_modify_post, name='room_modify_post'),
    path('<int:pk>/task', views.TaskView.as_view(), name='task_create'),
    path('task_post', views.TaskView.task_post, name='task_post'),
    path('task_list', views.TaskListView.as_view(), name='task_list'),
    path('<int:pk>/task_detail', views.TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/room_top', views.RoomTopView.as_view(), name='room_top'),
    path('<int:room_id>/<int:pk>/task_modify', views.TaskModifyView.as_view(), name='task_modify'),
    path('task_modify_post', views.TaskModifyView.task_modify_post, name='task_modify_post'),
    path('user/create', views.UserCreateView.as_view(), name='user_create'),
    path('user/create_post', views.UserCreateView.create_post, name='user_create_post'),
    path('user/detail/<int:pk>', views.UserDetailView.as_view(), name='user_detail'),
    path('user/my_page/<int:pk>', views.UserMyPageView.as_view(), name='user_my_page'),
]
