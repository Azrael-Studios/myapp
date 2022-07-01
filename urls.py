from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('classes/', views.Lclasses, name="classes"),
    path('classes/add/', views.makeClass, name="newclass"),
    path('classes/add/addrecord/', views.createClass, name="createClass"),
    path('classes/list/<int:id>', views.editList, name="editList"),
    path('students/', views.students, name="students"),
    path('students/add/', views.addStudent, name="add"),
    path('students/add/addrecord/', views.addrecord, name="addrecord"),
    path('homework/', views.homework, name="homework"),
    path('homework/add', views.makeHomework, name="createhomework"),
    path('homework/add/addrecord/', views.newHomework, name="makeHomework")
]