from django import forms
from django.db.models import fields
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MentorRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Mentor
        fields = ['fullname', 'age', 'gender', 'email', 'phone', 'spes']

class CourseRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = ['name', 'spes', 'mentor', 'student_qty', 'start', 'finish', 'price', 'status']

class StudentRegistrationForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['fullname', 'age', 'gender', 'email', 'phone', 'course', 'payment']

class LessonRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Lesson
        fields = ['data', 'time', 'room', 'course', 'student_qty', 'mentor', 'theme', 'status']

class Student_checkoutRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Lesson
        fields = ['course', 'time', 'room', 'data', 'student_qty', 'mentor', 'theme', 'status']