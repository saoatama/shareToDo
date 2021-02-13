from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from django.template import loader

from .models import Room, User, Task, Participant, Category, UserRoomRelation

# Create your views here.
def index(request):
	 return HttpResponse("You're voting on question")
def post(request):
    cate = Category.objects.create(category_name=request.POST['category_name'])
    return HttpResponse(request.POST['category_name'])

class RoomView(generic.TemplateView):
	model = Room
	template_name = 'shareToDo/room/post.html'
	def room_post(request):
		room = Room.objects.create(room_name=request.POST['room_name'], open_close=request.POST['open_close'])
		return HttpResponse(request.POST['room_name'])
class RoomModifyView(generic.DetailView):
	model = Room
	template_name = 'shareToDo/roomModify/post.html'

	def room_modify_post(request):
		room = Room.objects.get(id=request.POST['id'])
		room.room_name = request.POST['room_name']
		room.open_close = request.POST['open_close']
		room.save()
		return HttpResponse(request.POST['room_name'])
class RoomTopView(generic.ListView):
	template_name = 'shareToDo/room/list.html'
	model = Room
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		room = Room.objects.get(id=self.kwargs['pk'])
		context['room'] = room
		context['list'] = UserRoomRelation.objects.filter(room_id=room)
		context['task_list'] = Task.objects.filter(room=room)
		return context

class TaskView(generic.TemplateView):
	model = Task
	template_name = 'shareToDo/task/create.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		room = Room.objects.get(id=self.kwargs['pk'])
		context['room'] = room
		context['users'] = UserRoomRelation.objects.filter(room_id=room)
		context['categories'] = Category.objects.all()
		return context

	def task_post(request):
		category = Category.objects.get(id=request.POST['category'])
		author = User.objects.get(id=request.POST['author'])
		deadline =deadline=request.POST['deadline']
		room = Room.objects.get(id=request.POST['room'])
		if deadline == "":
			task = Task.objects.create(task_name=request.POST['task_name'], author=author, category=category, room=room)
		else:
			task = Task.objects.create(task_name=request.POST['task_name'], deadline=deadline, author=author, category=category, room=room)
		target_users = request.POST.getlist('target_user')
		worker_users = request.POST.getlist('worker_user')
		for user in target_users:
			target_user = User.objects.get(id=user)
			particioant = Participant.objects.create(user=target_user, task=task, role=1)
		for user in worker_users:
			worker_user = User.objects.get(id=user)
			particioant = Participant.objects.create(user=worker_user, task=task, role=2)
		return HttpResponse("done")

class TaskListView(generic.ListView):
	model = Task
	context_object_name = 'task_list'
	template_name = 'shareToDo/task/list.html'
	def get_queryset(self):
		"""Return the last five published questions."""
		return Task.objects.all()
class TaskDetailView(generic.DetailView):
	model = Task
	template_name = 'shareToDo/task/show.html'

class CategoryView(generic.DetailView):
    model = Category
    template_name = 'shareToDo/post.html'
