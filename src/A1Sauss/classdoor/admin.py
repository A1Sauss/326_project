from django.contrib import admin
from classdoor.models import Course, Teacher, Review, University, ClassdoorUser, Subject

#version 2
#Zihang, Matt
#10/26/2018, 11/5/2018

@admin.register(Course)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'starRating', 'subject', 'averageGrade')
    #field = ['name', 'teacher', 'description', 'rating', 'review's] 

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    #the default for field is vertical so it is good enough for displaying them
    #using a list filter to sort results
    list_filter = ('title','date', 'courseOfReview')
    list_display = ('title', 'starRating', 'date', 'courseOfReview')

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

@admin.register(ClassdoorUser)
class ClassdoorUserAdmin(admin.ModelAdmin):
    #default display
    pass

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'universityName')
