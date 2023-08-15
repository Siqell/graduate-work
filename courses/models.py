from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Course(models.Model):
	name_course = models.CharField(max_length = 100)
	file_course = models.FileField(max_length = 100, upload_to = 'docx/', default = 'defaultDocxFile.docx')
	image = models.ImageField(max_length = 100, upload_to = 'image/', default = 'defaultImage.jpg')
	date_added = models.DateTimeField('date added course', default = now())
	creator_id = models.CharField(max_length=20)
	def __str__(self):
		return self.name_course

class Task(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	text_task = models.TextField()
	right_answer = models.CharField(max_length = 200)
	def __str__(self):
		return self.text_task

class Answer(models.Model):
	task = models.ForeignKey(Task, on_delete = models.CASCADE, default = '')
	user_answer = models.CharField(max_length = 1, default = '')
	user = models.ForeignKey(User, on_delete = models.CASCADE, default = '')
	def __str__(self):
		return self.task

class UserCourse(models.Model):
	course = models.ForeignKey(Course, on_delete = models.CASCADE)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	def __str__(self):
		return self.course

