from json import load
from multiprocessing import context
from re import L, sub, template
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import LClass, Student, Homework, Teacher
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

# LClasses is Class with an L. The L stands for learners.

def index(request):                                 #fine
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def Lclasses(request):                                #fine
    template = loader.get_template('classes.html')
    myClasses = LClass.objects.all().values()
    teacher = Teacher.objects.all().values()
    context = {
        'classes': myClasses,
        'teacher': teacher,
    }
    return HttpResponse(template.render(context, request))

def addStudent(request):                                #fine
    template = loader.get_template('addStudent.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):                                 # this creates a new student object in the database
    first = request.POST['first']
    last = request.POST['last']
    target = request.POST['target']
    grade = request.POST['grade']
    email = request.POST['email']
    other = request.POST['other']
    student = Student(
        fname = first,
        lname = last,
        targetGrade = target,
        grade = grade,
        parentEmail = email,
        other = other,
    )
    student.save()
    return HttpResponseRedirect(reverse('students'))

@csrf_protect
def makeClass(request):                                     #fine
    template = loader.get_template('new_class.html')
    teacher = Teacher.objects.all().values()
    context = {
        'teachers': teacher,
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def createClass(request):                                   #fine
    name = request.POST['name']
    teacherId = request.POST['teacher']
    teacher = Teacher.objects.get(id = teacherId)
    subject = request.POST['subject']
    newClass = LClass(
        name = name,
        teacher = teacher,
        subject = subject,
    )
    newClass.save()
    return HttpResponseRedirect(reverse('classes'))

def students(request):                                      #fine
    template = loader.get_template('students.html')
    myStudents = Student.objects.all().order_by('lname').values()
    context = {
        'students': myStudents,
    }
    return HttpResponse(template.render(context, request))

def editList(request, id):
    # this is meant to get the class list!! (it doesn't work yet).
    template = loader.get_template('classList.html')
    myclass = LClass.students.all()
    students = LClass.objects.filter(students = id)
    context = {
        'class': myclass,
        'students': students,
    }
    return HttpResponse(template.render(context))


def homework(request):
    template = loader.get_template("hlist.html") # the homework list template
    homework = Homework.objects.all().values()
    context = {
        'homework': homework,
    }
    return HttpResponse(template.render(context, request))

def makeHomework(request):
    template = loader.get_template('homework.html')
    students = Student.objects.all().values()
    teachers = Teacher.objects.all().values()
    context = {
        'students': students,
        'teachers': teachers,
    }
    return HttpResponse(template.render(context, request))

def newHomework(request):
    name = request.POST['name']
    studentID = request.POST['student']
    student = Student.objects.get(id = studentID)
    teacherID = request.POST['teacher']
    teacher = Teacher.objects.get(id = teacherID)
    task = request.POST['task']
    newHomework = Homework(
        name = name,
        student = student,
        teacher = teacher,
        task = task,
    )
    newHomework.save()
    return HttpResponseRedirect(reverse('homework'))
