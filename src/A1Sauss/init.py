from classdoor.models import Subject, Course, University, Review, Teacher, ClassdoorUser
from faker import Faker
from django.contrib.auth.models import User
from datetime import timedelta
from decimal import *
import textwrap

fake = Faker()

# grades = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]

# Create Subjects
subjects = [
    Subject(name="Computer Scence", abbreviation="CS"),
    Subject(name="Biology", abbreviation="BIO"),
    Subject(name="Mathematics", abbreviation="MATH"),
    Subject(name="English", abbreviation="ENG"),
]

# Save the subjects to the database
for subj in subjects:
    subj.save()

# Create Universities
unis = []

for i in range(1, 5):
    uName = "University of " + fake.city()
    uAddress = fake.address()

    uni = University(name=uName, location=uAddress)

    uni.save()

    for subj in subjects:
        uni.subjectsOffered.add(subj)

    uni.save()
    unis.append(uni)

# Create Courses
courses = []
for i in range(1, 10):
    subject = subjects[fake.random_int(0, len(subjects) - 1)]
    subject.save()
    uni = unis[fake.random_int(0, len(unis) - 1)]
    teachFirstName = fake.name().split()[0]
    teachLastName = fake.name().split()[1]

    cName = subject.abbreviation + str(fake.random_int(100, 500))
    cTeacher = Teacher(first_name=teachFirstName, last_name=teachLastName)
    cTeacher.save()
    cDesc = fake.text(1000)
    cAvgGrade = Decimal(1)
    cStarRating = Decimal(fake.random_int(0, 500)) / 100

    c = Course(name=cName,
              teacher=cTeacher,
              description=cDesc,
              averageGrade=cAvgGrade,
              starRating=cStarRating,
              subject=subject,
              university=uni)

    c.save()
    courses.append(c)

users = []
print("Generated users:")
for i in range(1,20):
    firstName = fake.first_name()
    lastName = fake.last_name()
    username = firstName.lower()[0] + lastName.lower() + str(fake.random_int(0,999))
    email = f"{username}@326.edu"
    password = lastName
    user = User.objects.create_user(username, email, password)
    user.first_name = firstName
    user.last_name = lastName
    user.save()
    users.append(user)
    print(f"  username: {username}, password: {password}")

#USE THIS TO INSERT DATA FOR EACH USER
cdoorusers = ClassdoorUser.objects.all()
for cUser in cdoorusers:
    cUser.school = unis[fake.random_int(0, len(unis)-1)]
    cUser.major = subjects[fake.random_int(0, len(subjects)-1)]
    cUser.profileImage = "profile-" + str(fake.random_int(1,16)) + ".gif"
    cUser.save()


# Create Reviews
reviews = []
for i in range(0, len(courses) - 1):
    currClass = courses[i]
    rGrade = Decimal(1)

    for j in range(1, fake.random_int(3, 20)):
        rStarRating = Decimal(fake.random_int(0, 500)) / 100
        rTitle = fake.text(25)
        rText = fake.text(200)
        rAuthor = cdoorusers[fake.random_int(0, len(cdoorusers)-1)]


        review = Review(title=rTitle,
                        text=rText,
                        gradeReceived=rGrade,
                        starRating=rStarRating,
                        courseOfReview=currClass,
                        author=rAuthor)

        review.save()
        reviews.append(review)

        currClass.reviews.add(review)
        currClass.save()

for eachUser in cdoorusers:
    toAdd =[]
    for eachReview in reviews:
        if(eachReview.author == eachUser):
            eachUser.reviewsWritten.add(eachReview)

print('Subjects:')
for s in Subject.objects.all():
    print(s)

print('\nUniversities:')
for u in University.objects.all():
    print(u)

print('\nClasses:')
for c in Course.objects.all():
    print(c)

print('\nReviews:')
for i in Review.objects.all():
    print(i)

username = "admin"
password = "admin"
email = "admin@admin.admin"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
message = f"""
====================================================================
The database has been setup with the following credentials:

  username: {username}
  password: {password}
  email: {email}

You will need to use the username {username} and password {password}
to login to the administrative webapp in Django.

Please visit http://localhost:8080/admin to login to the admin app.
Run the django server with:

  $ python3 manage.py runserver 0.0.0.0:8080"
====================================================================
"""
print(message)

