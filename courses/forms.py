from django import forms
from .models import Course, Task
from django.contrib.auth.models import User


class CreateCourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ['name_course', 'file_course', 'image']
	def __init__(self, *args, **kwargs):
		super(CreateCourseForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'input__file'





class AddTaskToCourse(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['course', 'text_task', 'right_answer']
		widgets = {
			'text_task' : forms.TextInput(attrs={'class' : 'text-task'})
		}
	def __init__(self, *args, user_id, **kwargs):
		self.user_id = kwargs.get('user_id')
		
		super().__init__(*args, **kwargs)
		self.fields['course'].empty_label = "Выберите курс"
		self.fields['course'].queryset = Course.objects.filter(creator_id=user_id)

