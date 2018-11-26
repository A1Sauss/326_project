from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#Version 1.4
#Matt, Zander, Zihang
#10/26/2018, 11/15/2018

#-------------------part 1------------------------#

class Course(models.Model):
   """Model representing a specific class"""
   name = models.CharField(max_length=200)
   teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
   description = models.TextField(max_length=500, help_text = "Description of the course")
   #needs a method to calculate average rating
   starRating = models.DecimalField(max_digits=2, decimal_places=1)
   #changed reviews back to manytomany field
   reviews = models.ManyToManyField('Review', help_text="Select a review for this class", blank=True)
   #changed grade range
   'Not sure if we need grade for the class since we have grade in review'
   averageGrade = models.DecimalField(max_digits=2, decimal_places=1)
   #needs to be able to choose multiple preReqs
   'preReq needs to be fullfilled with other classes, requires more work to implement it'
   #preReq = models.ManyToManyField('PreReq', help_text="Select a preReq for this class", blank=True)
   subject = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True)
   university_name = models.ForeignKey('University', on_delete=models.SET_NULL, null=True)
   'likes and dislikes are designed to vote for reviews, needs to consult with others about how to implement it'
   #likes = models.IntegerField(default=0)
   #dislikes = models.IntegerField(default=0)

   class Meta:
       ordering = ['name']

   def get_absolute_url(self):
       """Returns the url to access a particular class."""
       return reverse('class-detail', args=[str(self.id)])

   def __str__(self):
       """String for representing the Model object."""
       return f'{self.name}'

#-------------------part 2------------------------#

class Teacher(models.Model):
   """Model representing a teacher."""
   first_name = models.CharField(max_length=100)
   last_name = models.CharField(max_length=100)

   class Meta:
      ordering = ['last_name', 'first_name']

   def get_absolute_url(self):
      """Returns the url to access a particular teacher."""
      return reverse('teacher-detail', args=[str(self.id)])

   def __str__(self):
      """String for representing the Model object."""
      return f'{self.last_name}, {self.first_name}'

#-------------------part 3------------------------#
   
class Review(models.Model):
   """Model representing a review."""
   grade_choices = (('a','A'), ('a-', 'A-'), ('b+','B+'), ('b','B'), ('b-','B-'), ('c+', 'C+'), ('c', 'C'), ('c-', 'C-'), ('d+', 'D+'), ('d', 'D'), ('d', 'D-'), ('f', 'F'))
   tag_choices = (('easy','Easy'), ('hard','Hard'), ('Interesting','Interesting'), ('boring','Boring'), ('attendence','Attendence Graded'), ('gen-ed','Gen-Ed'), ('professor','Great Professsor'), ('homework','Lots of Homework'), ('exam', 'Exam-Heavy'))
   star_choices= (('5','5'),('4','4'),('3','3'),('2','2'),('1','1'))

   title = models.CharField(max_length=200)
   text = models.TextField(max_length=500)
   #will figure out how to put a range on the rating
   #decimal fields do not take a default
   starRating = models.CharField(max_length=3, choices = star_choices);

   gradeReceived = models.CharField(max_length=2, choices = grade_choices, blank = True);

   date = models.DateField(null=True, blank=True)
   #will figure out how to create tags for people to choose instead of entering them
   tags = models.CharField(max_length=100, choices = tag_choices, blank = True);
   #tags = models.ManyToManyField('Tags', help_text="Select tags for this class", blank=True)
   courseOfReview = models.ForeignKey('Course', help_text="Select a course for this description",  on_delete=models.SET_NULL, null=True)
   author = models.ForeignKey('ClassdoorUser', on_delete=models.SET_NULL, null=True, blank=True)
 
   class Meta:
       ordering = ['title']

   def get_absolute_url(self):
       """Returns the url to access a particular review."""
       return reverse('review-detail', args=[str(self.id)])

   def __str__(self):
       """String for representing the Model object."""
       return f'{self.title}'

#-------------------part 4------------------------#
 
class University(models.Model):
   """Model representing an university."""

   name = models.CharField(max_length=200)
   location = models.CharField(max_length=500)
   courses = models.ManyToManyField('Course')
   subjectsOffered = models.ManyToManyField('Subject', blank=True)   

   class Meta:
       ordering = ['name']

   def get_absolute_url(self):
       """Returns the url to access a particular university."""
       return reverse('university-detail', args=[str(self.id)])

   def __str__(self):
       """String for representing the Model object."""
       return f'{self.name}'

#-------------------part 5------------------------#
 
class ClassdoorUser(models.Model):
   """Model representing an user."""
   user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
   school = models.ForeignKey('University',  on_delete=models.SET_NULL, null=True, related_name='+')
   major = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True)
   profileImage = models.CharField(max_length=15, default='profile-1.gif')
   reviewsWritten = models.ManyToManyField('Review')
   
   class Meta:
       ordering = ['user']

   def get_absolute_url(self):
       """Returns the url to access a particular author instance."""
       return reverse('user-detail', args=[str(self.id)])

   def __str__(self):
       """String for representing the Model object."""
       return f'{self.user}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ClassdoorUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.classdooruser.save()

#-------------------part 6------------------------#
 
class Subject(models.Model):
   """Model representing a Subject."""

   name = models.CharField(max_length=40, default="SUBJECT")
   abbreviation = models.CharField(max_length=10, default="COURSE")
   #will figure out how to access the name in that class instead of the whole class
   universityName = models.ForeignKey('University',  on_delete=models.SET_NULL, null=True, related_name='+')
   
   class Meta:
       ordering = ['name']

   def get_absolute_url(self):
       """Returns the url to access a particular subject."""
       return reverse('subject-detail', args=[str(self.id)])

   def __str__(self):
       """String for representing the Model object."""
       return f'{self.name}'

"""#-------------------part 7------------------------#
 
class Tags(models.Model):
   #Model representing Tags.

   tag_choices = (('easy','Easy'), ('hard','Hard'), ('Interesting','Interesting'), ('boring','Boring'), ('attendence','Attendence Graded'), ('gen-ed','Gen-Ed'), ('professor','Great Professsor'), ('homework','Lots of Homework'), ('exam','Exam-Heavy'))
   tags = models.CharField(max_length=100, choices = tag_choices, blank = True);
   courseOfTag = models.ForeignKey('Course', help_text="Select a course for this description",  on_delete=models.SET_NULL, null=True)
   class Meta:
       ordering = ['tags']

   def __str__(self):
       #String for representing the Model object.
       return f'{self.name}'

       """