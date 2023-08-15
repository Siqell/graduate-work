from django.shortcuts import render
from courses.models import Course, UserCourse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import Group

def index(request):
	all_courses_list = Course.objects.all()
	three_courses_in_start = []
	if all_courses_list != None  and len(all_courses_list) >= 3:
		for i in range(3):
			three_courses_in_start.append(all_courses_list[i])

	context = {
			'three_courses_in_start' : three_courses_in_start,
		}
	return render(request, 'mainpage/index.html', context)



def about(request):
	return render(request, 'about/about.html')



def profile(request):
	courses_create_this_pepod = Course.objects.filter(creator_id = request.user.id)

	id_courses_this_user = UserCourse.objects.filter(user_id = request.user.id)
	id_courses = []

	for Id in id_courses_this_user:
		id_courses.append(Id.course_id)
	courses_this_user = []


	for Id in id_courses:
		courses_this_user.append(Course.objects.get(pk = Id))

	user = User.objects.get(pk = request.user.id)
	groups = user.groups.all()
	group = str(groups.get())

	

	context = {
		'courses_create_this_pepod' : courses_create_this_pepod,
		'group' : group,
		'courses_this_user' : courses_this_user,
	}
	return render(request, 'registration/profile.html', context)



def regpage(request):
	return render(request, 'registration/registration.html')






def signup(request):
	username = request.POST['username']
	email = request.POST['email']
	password = request.POST['password']
	if password != '':
		password = make_password(password)
	check_unique_username = User.objects.filter(username = username)
	check_unique_email = User.objects.filter(email = email)
	if not (username == '' or email == '' or password == ''):
		if not check_unique_username:
			if not check_unique_email:
				new_user = User(username = username, email = email, password = password, is_active = 1, is_superuser = 0)
				new_user.save()
				user = User.objects.last()
				my_group = Group.objects.get(name='user')
				my_group.user_set.add(user)
				return HttpResponseRedirect(reverse('auth:login'))
		elif (not check_unique_username) and (check_unique_email):
			return HttpResponseRedirect(reverse('mainpage:regpage'))
		elif (check_unique_username) and  (not check_unique_email):
			return HttpResponseRedirect(reverse('mainpage:regpage'))
		else:
			return HttpResponseRedirect(reverse('mainpage:regpage'))
	else:
		return HttpResponseRedirect(reverse('mainpage:regpage'))


