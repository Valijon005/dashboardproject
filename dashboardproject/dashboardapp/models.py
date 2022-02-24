from django.db import models
from django.db.models.deletion import SET_NULL



class Mentor(models.Model):
    GENDER_CHOICE = [
        ("M", "M"),
        ("F", "F"),
    ]
    SPES_CHOICE = [
        ("FRONTEND", "FRONTEND"),
        ("BACKEND", "BACKEND"),
    ]
    fullname = models.CharField(max_length=90)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, default="M")
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    spes = models.CharField(max_length=9, choices=SPES_CHOICE, default="SPES_CHOICE")
    # photo = models.ImageField(blank=True, null=True, upload_to="mentors/")

    def __str__(self):
        return self.fullname

class Course(models.Model):
    SPES_CHOICE = [
        ("HTML", "HTML"),
        ("JS", "JS"),
        ("PYTHON", "PYTHON"),
        ("REACT", "REACT"),
        ("DJANGO", "DJANGO"),
    ]
    STATUS_CHOICE = [
        ("NO", "NO"),
        ("FULL", "FULL"),
        ("PART", "PART"),
    ]
    name = models.CharField(max_length=50)
    spes = models.CharField(max_length=7, choices=SPES_CHOICE, default="HTML")
    mentor = models.ForeignKey(Mentor, on_delete=SET_NULL, null=True, blank=True)
    student_qty = models.PositiveIntegerField(blank=True, null=True)
    start = models.DateField(blank=True, null=True)
    finish = models.DateField(blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    status = models.CharField(max_length=5, choices=STATUS_CHOICE, default="NO")

    def __str__(self):
        return self.name

    def total_payment(self):
        return self.student_qty * self.price

class Student(models.Model):
    GENDER_CHOICE = [
        ("M", "M"),
        ("F", "F"),
    ]
    PAYMENT_CHOICE = [
        ("NO", "NO"),
        ("YES", "YES"),
    ]
    fullname = models.CharField(max_length=90)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, default="M")
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    course = models.ForeignKey(Course, on_delete=SET_NULL, null=True, blank=True)
    payment = models.CharField(max_length=4, choices=PAYMENT_CHOICE, default="NO")

    def __str__(self):
        return self.fullname

class Lesson(models.Model):
    TIME_CHOICE = [
        ("11:00-12:30", "11:00-12:30"),
        ("14:00-15:30", "14:00-15:30"),
        ("16:00-17:30", "16:00-17:30"),
        ("18:30-20:00", "18:30-20:00"), 
    ]
    ROOM_CHOICE = [
        ("FIRST", "FIRST"),
        ("SECOND", "SECOND"),
        ("COWORKING", "COWORKING"),
    ]
    STATUS_CHOICE = [
        ("PLANNED", "PLANNED"),
        ("DONE", "DONE"),
        ("CANCEL", "CANCEL"),
    ]
    data = models.DateField()
    time = models.CharField(max_length=13, choices=TIME_CHOICE, default="11:00-12:30")
    room = models.CharField(max_length=12, choices=ROOM_CHOICE, default="FIRST")
    course = models.ForeignKey(Course, on_delete=SET_NULL, null=True, blank=True)
    student_qty = models.PositiveIntegerField()
    mentor = models.ForeignKey(Mentor, on_delete=SET_NULL, null=True, blank=True)
    theme = models.CharField(max_length=90)
    status = models.CharField(max_length=8, choices=STATUS_CHOICE, default="PLANNED")

    def __str__(self):
        return self.time

# class Student_checkout(models.Model):
#     TIME_CHOICE = [
#         ("11:00-12:30", "11:00-12:30"),
#         ("14:00-15:30", "14:00-15:30"),
#         ("16:00-17:30", "16:00-17:30"),
#         ("18:30-20:00", "18:30-20:00"), 
#     ]
#     ROOM_CHOICE = [
#         ("FIRST", "FIRST"),
#         ("SECOND", "SECOND"),
#         ("COWORKING", "COWORKING"),
#     ]
#     STATUS_CHOICE = [
#         ("TO EXIST", "TO EXIST"),
#         ("NO", "NO"),
#         ("CAUSE", "CAUSE"),
#     ]
#     course = models.ForeignKey(Course, on_delete=SET_NULL, null=True, blank=True)
#     time = models.CharField(max_length=13, choices=TIME_CHOICE, default="11:00-12:30")
#     room = models.CharField(max_length=12, choices=ROOM_CHOICE, default="FIRST")
#     data = models.DateField()
#     student_qty = models.PositiveIntegerField()
#     mentor = models.ForeignKey(Mentor, on_delete=SET_NULL, null=True, blank=True)
#     theme = models.CharField(max_length=90)
#     status = models.CharField(max_length=8, choices=STATUS_CHOICE, default="NO")

#     def __str__(self):
#         return self.time