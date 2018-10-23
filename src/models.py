from django.db import models

class ClassDesc(models.Model):
   """Model representing a course profile."""
   name = models.CharField(max_length=200)
   teacher = models.CharField(max_length=200)
   description = models.CharField(max_length=200, help_text = "Description of the course")
   rating = models.DecimalField(default=0.0, max_digits=4, decimal_places=2)
   reviews = models.ForeignKey('Review', max_length = 500, on_delete = models.SET_NULL, null = True, help_text="Review for this class")
   grade = models.DecimalField(default=0.0, max_digits=4, decimal_places=2)
   preReqs = models.ManyToManyField('self', help_text="PreReqs for this class", blank=True)
   subjects = models.ForeignKey('Subject', help_text="Select a subject for this class",  on_delete=models.SET_NULL, null=True)
   universities = models.ForeignKey('University', max_length=200,  on_delete=models.SET_NULL, null=True)
   likes = models.IntegerField(default=0)
   dislikes = models.IntegerField(default=0)

   class Meta:
       ordering = ['name']

   def get_absolute_url(self):
       """Returns the url to access a particular class."""
       return reverse('class-detail', args=[str(self.id)])

   def __str__(self):
       """String for representing the ClassDesc object."""
       return f'{self.name}'

#-------------------part 1------------------------#
    
class Review(models.Model):
   """Model representing a review page."""
   title = models.CharField(max_length=200)
   text = models.CharField(max_length=500)
   starRating = models.DecimalField(max_digits=3, decimal_places=2)
   gradeReceived = models.DecimalField(max_digits=3, decimal_places=2)
   date = models.DateField(null=True, blank=True)
   tags = models.CharField(max_length = 10, help_text = "Describe course difficulty as easy/medium/hard/fun/boring/netural")
   #classDesc = models.ForeignKey('ClassDesc', help_text="Select a class for this description",  on_delete=models.SET_NULL, null=True)
   author = models.ForeignKey('User', help_text="Select a user for this review",  on_delete=models.SET_NULL, null=True)
 
   class Meta:
       ordering = ['title']

   def get_absolute_url(self):
       """Returns the url to access a particular review."""
       return reverse('review-detail', args=[str(self.id)])

   def __str__(self):
       """String for representing the Review object."""
       return f'{self.title}'

#-------------------part 2------------------------#
 
class University(models.Model):
   """Model representing an library event."""

   name = models.CharField(max_length=200)
   location = models.CharField(max_length=500)
   classes = models.ManyToManyField('ClassDesc')
   subjectsOffered = models.ManyToManyField('Subject', blank=True)   

   class Meta:
       ordering = ['name']

   def get_absolute_url(self):
       """Returns the url to access a particular university."""
       return reverse('university-detail', args=[str(self.id)])

   def __str__(self):
       """String for representing the University object."""
       return f'{self.name}'

#-------------------part 3------------------------#
 
class User(models.Model):
   """Model representing an library event."""

   username = models.CharField(max_length=15)
   email = models.CharField(max_length=30)
   password = models.CharField(max_length=20)
   major = models.ManyToManyField('Subject')
   writtenReviews = models.ManyToManyField('Review', blank=True)
   
   class Meta:
       ordering = ['username']

   def get_absolute_url(self):
       """Returns the url to access a particular author instance."""
       return reverse('user-detail', args=[str(self.id)])

   def __str__(self):
       """String for representing the User object."""
       return f'{self.username}'

#-------------------part 4------------------------#
 
class Subject(models.Model):
   """Model representing an library event."""

   name = models.CharField(max_length=40)
   universityName = models.ForeignKey('University',  on_delete=models.SET_NULL, null=True, related_name='+')
   
   class Meta:
       ordering = ['name']

   def get_absolute_url(self):
       """Returns the url to access a particular subject."""
       return reverse('subject-detail', args=[str(self.id)])

   def __str__(self):
       """String for representing the Subject object."""
       return f'{self.name}'




