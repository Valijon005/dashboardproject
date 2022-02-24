from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

@login_required(login_url='login')
def base(request):
    return render(request, "dashboardapp/mentor_account.html")

@login_required(login_url='login')
def mentor_account(request):
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('login')

    context = {'form':form}
    return render(request, 'dashboardapp/mentor_account.html', context)
    
@login_required(login_url='login')
def student_account(request):
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('login')

    context = {'form':form}
    return render(request, 'dashboardapp/student_account.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, "ERORR")
            
        context = {}

        return render(request, 'dashboardapp/login.html', context)

@login_required(login_url='login')
def students_table(request):
    students = Student.objects.all()[::-1]
    courses = Course.objects.all()

    if request.method == 'POST' and request.POST.get('course_id'):
        students = Student.objects.filter(course=request.POST.get('course_id'))
    else:
        students = Student.objects.all()

    context = {
        'students': students,
        'courses': courses,
    }
    return render(request, "dashboardapp/students_table.html", context)

@login_required(login_url='login')
def groups_table(request):
    courses = Course.objects.all()[::-1]
    mentors = Mentor.objects.all()
    # payment_sum = courses.student_qty * courses.price
    if request.method == 'POST' and request.POST.get('mentor_id'):
        courses = Course.objects.filter(mentor=request.POST.get('mentor_id'))
    else:
        courses = Course.objects.all()
    context = {
        'courses': courses,
        'mentors': mentors,
        # 'payment_sum': payment_sum,
    }
    return render(request, "dashboardapp/groups_table.html", context)

@login_required(login_url='login')
def lessons_table(request):
    lessons = Lesson.objects.all()[::-1]
    mentors = Mentor.objects.all()
    courses = Course.objects.all()

    if request.method == 'POST' and request.POST.get('mentor_id'):
        lessons = Lesson.objects.filter(mentor=request.POST.get('mentor_id'))
    elif request.method == 'POST' and request.POST.get('course_id'):
        lessons = Lesson.objects.filter(course=request.POST.get('course_id'))
    else:
        lessons = Lesson.objects.all()
    context = {
        'lessons': lessons,
        'mentors': mentors,
        'courses' : courses,
    }
    return render(request, "dashboardapp/lessons_table.html", context)


@login_required(login_url='login')
def dashboard(request):
    students = Student.objects.all()
    lessons = Lesson.objects.all()
    courses = Course.objects.all()
    mentors = Mentor.objects.all()
    student_qty = students.count()
    courses_qty = courses.count()
    lessons_qty = lessons.count()
    if request.method == 'POST' and request.POST.get('course_id'):
        students = Student.objects.filter(course=request.POST.get('course_id'))
    else:
        students = Student.objects.all()

    if request.method == 'POST' and request.POST.get('mentor_id'):
        courses = Course.objects.filter(mentor=request.POST.get('mentor_id'))
    else:
        courses = Course.objects.all()

    if request.method == 'POST' and request.POST.get('mentor_id'):
        lessons = Lesson.objects.filter(mentor=request.POST.get('mentor_id'))
    else:
        lessons = Lesson.objects.all()

    context = {
        'students': students,
        'lessons': lessons,
        'courses': courses,
        'mentors': mentors,
        'student_qty' : student_qty, 
        'courses_qty' : courses_qty,
        'lessons_qty' : lessons_qty
    }
    return render(request, "dashboardapp/index.html", context)

@login_required(login_url='login')
def add_course(request):
    
    if request.method == 'POST':
        
        form = CourseRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    
    else:
        form = CourseRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'dashboardapp/add_course.html', context)

@login_required(login_url='login')
def updateCourse(request, pk):
    course = Course.objects.get(id=pk)
    form  = CourseRegistrationForm(instance=course)
    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('groups_table')

    context = {
        'form': form
    }
    return render(request, 'dashboardapp/add_course.html', context)

@login_required(login_url='login')
def deleteCourse(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == "POST":
        course.delete()
        return redirect('groups_table') 
    context = {
        'course': course
    }
    return render(request, 'dashboardapp/delete_course.html', context)

@login_required(login_url='login')
def add_mentor(request):
    
    if request.method == 'POST':
        
        form = MentorRegistrationForm(request.POST, request.FILES)

        
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    
    else:
        form = MentorRegistrationForm()

    context = {
        'form': form
    }

    return render(request, "dashboardapp/add_mentor.html", context)

@login_required(login_url='login')
def add_student(request):
    
    if request.method == 'POST':
        
        form = StudentRegistrationForm(request.POST)
        
        if form.is_valid():
           
            form.save()
            return redirect('dashboard')

    
    else:
        form = StudentRegistrationForm()

    return render(request, "dashboardapp/add_student.html", {'form': form})

@login_required(login_url='login')
def updateStudent(request, pk):
    student = Student.objects.get(id=pk)
    form  = StudentRegistrationForm(instance=student)
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students_table')

    context = {
        'form': form
    }
    return render(request, 'dashboardapp/add_student.html', context)

def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        return redirect('students_table') 
    context = {
        'student' : student
    }
    return render(request, 'dashboardapp/delete_student.html', context)

@login_required(login_url='login')
def add_lesson(request):
    
    if request.method == 'POST':
        
        form = LessonRegistrationForm(request.POST)
        
        if form.is_valid():
           
            form.save()
            return redirect('dashboard')

    
    else:
        form = LessonRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'dashboardapp/add_lesson.html', context)

@login_required(login_url='login')
def updateLesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    form  = LessonRegistrationForm(instance=lesson)
    if request.method == 'POST':
        form = LessonRegistrationForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('lessons_table')

    context = {
        'form': form
    }
    return render(request, 'dashboardapp/add_lesson.html', context)

@login_required(login_url='login')
def deleteLesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    if request.method == "POST":
        lesson.delete()
        return redirect('lessons_table') 
    context = {
        'lesson' : lesson
    }
    return render(request, 'dashboardapp/delete_lesson.html', context)

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')

# @login_required(login_url='login')
# def checkouts(request):
#     checkouts = Student_checkout.objects.all()[::-1]
#     mentors = Mentor.objects.all()
#     courses = Course.objects.all()
#     students = Student.objects.filter(course.request.POST.get('course_id'))
#     if request.method == 'POST':
#         if request.method == 'POST' and request.POST.get('mentor_id'):
#             checkouts = Student_checkout.objects.filter(mentor=request.POST.get('mentor_id'))
#         elif request.method == 'POST' and request.POST.get('course_id'):
#             checkouts = Student_checkout.objects.filter(course=request.POST.get('course_id'))
#             students = Student.objects.filter(course.request.POST.get('course_id'))
#         else:
#             checkouts = Student_checkout.objects.all()
#         return redirect('checkout')
#     context = {
#         'checkouts' : checkouts,
#         'mentors': mentors,
#         'courses' : courses,
#     }
#     return render(request, 'dashboardapp/checkout.html', context)

     
    
@login_required(login_url='login')
def students_inLesson(request):
    students = Student.objects.all()[::-1]
    courses = Course.objects.all()

    if request.method == 'POST' and request.POST.get('course_id'):
        students = Student.objects.filter(course=request.POST.get('course_id'))
    else:
        students = Student.objects.all()

    context = {
        'students': students,
        'courses': courses,
    }
    return render(request, "dashboardapp/students_table.html", context)
   