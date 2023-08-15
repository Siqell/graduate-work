from django.urls import path

from . import views


app_name = 'courses'
urlpatterns = [
	path('', views.courses, name = 'courses'),
	path('<int:id_course>/', views.courseView, name = 'courseView'),
	path('<int:id_course>/tasks/', views.tasks, name = 'tasks'),
	path('<int:id_course>/tasks/check_answer/', views.check_answer, name = 'check_answer'),
	path('record/', views.record, name = 'record'),
	path('manage_record/', views.manage_record, name = 'manage_record'),
	path('delete_record/', views.delete_record, name = 'delete_record'),
	path('create_course_page/', views.create_course_page, name = 'create_course_page'),
	path('create_course/', views.create_course, name = 'create_course'),
	path('add_task_to_course_page/', views.add_task_to_course_page, name = 'add_task_to_course_page'),
	path('add_task_to_course/', views.add_task_to_course, name = 'add_task_to_course'),
	path('course_results/<int:id_course>/', views.course_results, name = 'course_results'),
]