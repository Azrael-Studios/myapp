from audioop import maxpp
from multiprocessing.dummy import Array
from operator import mod
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Student(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    parentEmail = models.CharField(max_length=30)
    grade = models.IntegerField()
    targetGrade = models.IntegerField()
    other = models.CharField(max_length=255)
    def __str__(self):
        return self.fname
    class Meta:
        ordering = ['lname']

class LClass(models.Model):
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def students(self):
        return self.students
    class Meta:
        ordering = ['name']

class Homework(models.Model):
    name = models.CharField(max_length=40)
    task = models.CharField(max_length=255)
    grade = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class ClassList(models.Model):
    student_id = models.ForeignKey(Student, related_name="name", on_delete=models.CASCADE)
    lclass_id = models.ForeignKey(LClass, related_name="lclass", on_delete=models.CASCADE)
