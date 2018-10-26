from django.db import models

#Version 1.4
#Description: some modifications are added into the model, a new class teacher was created
#Matt, Zander, Zihang
#10/26/2018

#-------------------part 1------------------------#

class Class(models.Model):
   """Model representing a specific class"""
   name = models.CharField(max_length=200)
   #change teacher to foreign key
   teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
   #change description to text field
   description = models.TextField(max_length=500, help_text = "Description of the course")
   #chaged rating range
   #also needs a method to calculate average rating
   rating = models.DecimalField(default=0.0, max_digits=2, decimal_places=1)
   #changed reviews back to manytomany field
   review = models.ManyToManyField('Review', help_text="Select a review for this class")
   #changed grade range
   'Not sure if we need grade for the class since we have grade in review'
   #grade = models.DecimalField(default=0.0, max_digits=2, decimal_places=1)
   #changed self to PreReq
   #also needs to be able to choose multiple preReqs
   'preReq needs to be fullfilled with other classes, requires more work to implement it'
   #preReq = models.ManyToManyField('PreReq', help_text="Select a preReq for this class", blank=True)
   subject = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True)
   university = models.ForeignKey('University', on_delete=models.SET_NULL, null=True)
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
      return f'{self.last_name}, {self.first_name}

#-------------------part 3------------------------#
   
class Review(models.Model):
   """Model representing a review."""
   title = models.CharField(max_length=200)
   #changed charfield to textfield
   text = models.TextField(max_length=500, help_text='Enter your review for this class')
   #will figure out how to put a range on the rating
   starRating = models.DecimalField(max_digits=2, decimal_places=1)
   #not sure grade using numbers? will figure out how to properly present grade
   gradeReceived = models.DecimalField(max_digits=2, decimal_places=1)
   date = models.DateField(null=True, blank=True)
   #will figure out how to create tags for people to choose instead of entering them
   tags = models.CharField(max_length = 10, help_text = "Describe course difficulty as easy/medium/hard/fun/boring/netural")
   #since we have review as foreignkey in class model I(Zihang) felt we may not need to add ClassDesc here
   #classDesc = models.ForeignKey('ClassDesc', help_text="Select a class for this description",  on_delete=models.SET_NULL, null=True)
   #will figure out the proper way to automatically add author info since every review is not anonymous or written through different accounts
   author = models.ForeignKey('User', help_text="Select a user for this review",  on_delete=models.SET_NULL, null=True)
 
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
   classes = models.ManyToManyField('Class')
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
 
class User(models.Model):
   """Model representing an user."""

   username = models.CharField(max_length=15)
   email = models.CharField(max_length=30)
   password = models.CharField(max_length=20)
   #will figure out how to properly represent the major of the user
   major = models.ManyToManyField('Subject')
   writtenReviews = models.ManyToManyField('Review', blank=True)
   
   class Meta:
       ordering = ['username']

   def get_absolute_url(self):
       """Returns the url to access a particular author instance."""
       return reverse('user-detail', args=[str(self.id)])

   def __str__(self):
       """String for representing the Model object."""
       return f'{self.username}'

#-------------------part 6------------------------#
 
class Subject(models.Model):
   """Model representing a Subject."""

   name = models.CharField(max_length=40)
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



