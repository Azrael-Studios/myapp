from django.contrib import admin
from .models import Teacher, Student, Homework, LClass

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Homework)
admin.site.register(LClass)