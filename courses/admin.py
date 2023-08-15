from django.contrib import admin
from .models import Course, Task, Answer, UserCourse

admin.site.register(Course)
admin.site.register(Task)
admin.site.register(Answer)
admin.site.register(UserCourse)