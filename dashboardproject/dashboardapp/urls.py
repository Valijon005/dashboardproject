from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('base', views.base, name="base"),
    path('add_student', views.add_student, name="add_student"),
    path('add_course', views.add_course, name="add_course"),
    path('add_mentor', views.add_mentor, name="add_mentor"),
    path('add_lesson', views.add_lesson, name="add_lesson"),
    path('students_table', views.students_table, name="students_table"),
    path('groups_table', views.groups_table, name="groups_table"),
    path('lessons_table', views.lessons_table, name="lessons_table"),
    path('students_in_lesson', views.students_inLesson, name="students_in_lesson"),
    path('login', views.login_page , name="login"),
    path('logout', views.logout_user , name="logout"),
    path('mentor_account', views.mentor_account, name="mentor_account"),
    path('student_account', views.student_account, name="student_account"),
    path('update/<str:pk>/', views.updateCourse, name="update"),
    path('delete_course/<str:pk>/', views.deleteCourse, name="delete_course"),
    path('student/<str:pk>/', views.updateStudent, name="student"),
    path('delete_student/<str:pk>/', views.deleteStudent, name="delete_student"),
    path('lesson/<str:pk>/', views.updateLesson, name="lesson"),
    path('delete_lesson/<str:pk>/', views.deleteLesson, name="delete_lesson"),

]