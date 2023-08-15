from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import docx
from .forms import CreateCourseForm, AddTaskToCourse

from .models import Course, Task, UserCourse, Answer
from django.contrib.auth.models import User

def courses(request):
	all_courses_list = Course.objects.all()
	if request.user.is_authenticated:
		user = User.objects.get(pk = request.user.id)
		groups = user.groups.all()
		group = str(groups.get())
	else:
		group = ''

	context = {
		'all_courses_list': all_courses_list,
		'group' : group,
	}
	return render(request, 'courses/courses.html', context)

def courseView(request, id_course):
	this_course = Course.objects.get(id = id_course)
	file = this_course.file_course
	docx_file = docx.Document(file)
	text_course = docx_file.paragraphs


	context = {
		'text_course' : text_course,
		'id_course' : id_course,
		'this_course' : this_course,
	}
	return render(request, 'courses/course.html', context)

def tasks(request, id_course):
	course_name = Course.objects.get(id = id_course).name_course
	all_tasks_this_course = Task.objects.filter(course_id = id_course)
	all_answer_this_user = Answer.objects.filter(user_id = request.user.id)
	context ={
		'all_tasks_this_course' : all_tasks_this_course,
		'all_answer_this_user' : all_answer_this_user,
		'id_course' : id_course,
		'course_name' : course_name,
		}
	return render(request, 'tasks/tasks.html', context)

def check_answer(request, id_course):
	all_tasks_this_course = Task.objects.filter(course_id = id_course)
	id_task = int(request.POST['id'])
	this_task = all_tasks_this_course.get(id = (id_task))
	user_answer = request.POST['answer']
	user_id = request.user.id
	if user_answer == this_task.right_answer:
		user_answer = '1'
	else:
		user_answer = '0'
	ans = Answer.objects.filter(user_id = user_id)
	ans = ans.filter(task_id = id_task)

	if not(ans):
		answer = Answer(task_id = id_task, user_answer = user_answer, user_id = user_id)
		answer.save()
	else:
		ans = ans[0]
		ans.user_answer = user_answer
		ans.save()
	return HttpResponseRedirect(reverse('courses:tasks', args = [id_course]))



def record(request):
	user = request.user
	id_this_course = request.POST['id_course']
	courses_this_user = UserCourse.objects.filter(user_id = user.id)
	i = 0
	if courses_this_user:
		for course in courses_this_user:
			if int(id_this_course) == int(course.course_id):
				i = i + 1
		if i == 0:
			record_course = UserCourse(course_id = id_this_course, user_id = user.id)
			record_course.save()
	else:
		record_course = UserCourse(course_id = id_this_course, user_id = user.id)
		record_course.save()
	return HttpResponseRedirect(reverse('courses:courses'))



def manage_record(request):
	id_courses_this_user = UserCourse.objects.filter(user_id = request.user.id)
	id_courses = []
	for Id in id_courses_this_user:
		id_courses.append(Id.course_id)
	courses_this_user = []
	for Id in id_courses:
		courses_this_user.append(Course.objects.get(pk = Id))
	if courses_this_user == []:
		return HttpResponseRedirect(reverse("mainpage:profile"))
	context = {
		'courses_this_user' : courses_this_user,
	}

	
	return render(request, 'courses/manage_courses.html', context)


def delete_record(request):
	courses_this_user = UserCourse.objects.filter(user_id = request.user.id)
	course = courses_this_user.get(course_id = request.POST['id_course'])
	course.delete()

	return HttpResponseRedirect(reverse('courses:manage_record'))



def create_course_page(request):
	form = CreateCourseForm()
	user_id = request.user.id
	context = {
		'user_id' : user_id,
		'form': form, 
		}
	return render(request, 'courses/create_course_page.html', context)


def create_course(request):
	if request.method == 'POST':
		creator_id = request.POST['creator_id']
		form = CreateCourseForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			last_course = Course.objects.last()
			last_course.creator_id = creator_id
			last_course.save()
			return HttpResponseRedirect(reverse('courses:create_course_page'))
	return HttpResponseRedirect(reverse('courses:create_course_page'))



def add_task_to_course_page(request):
	form = AddTaskToCourse(user_id=request.user.id)
	return render(request, 'courses/add_task_to_course_page.html', {'form': form,})

def add_task_to_course(request):
	if request.method == 'POST':
		form = AddTaskToCourse(request.POST, user_id=request.user.id)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('courses:add_task_to_course_page'))
	else:
		form = AddTaskToCourse(user_id=request.user.id)
	return HttpResponseRedirect(reverse('courses:create_course_page'))



def course_results(request, id_course):
	tasks_this_course = Task.objects.filter(course_id = id_course)
	all_results = []
	for task in tasks_this_course:
		answers_this_task = Answer.objects.filter(task_id = task.id)
		for answer in answers_this_task:
			all_results.append(answer)
	course_name = Course.objects.get(id = id_course).name_course
	context = {
		'tasks_this_course' : tasks_this_course,
		'all_results' : all_results,
		'course_name' : course_name,
	}
	return render(request, 'courses/all_results.html', context)