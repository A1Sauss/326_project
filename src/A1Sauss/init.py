from classdoor.models import Subject, Course, University, Review, Teacher, ClassdoorUser
from django.contrib.contenttypes.models import ContentType
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

for i in range(1, 3):
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

# Create and add users
users = []
print("Generated users:")
for i in range(1,30):
    username = fake.first_name().lower()[0] + fake.last_name().lower()
    email = f"{username}@326.edu"
    password = username
    user = User.objects.create_user(username, email, password)
    user.first_name = fake.first_name()
    user.last_name = fake.last_name()
    user.save()
    users.append(user)
    print(f"  username: {username}, password: {password}")

# Create Courses
classdoorUsers = []
for cuser in users:
    uuser = cuser
    umajor = subjects[fake.random_int(0,len(subjects)-1)]
    umajor.save()
    uschool = unis[fake.random_int(0, len(unis) - 1)]
    uschool.save()

    u = ClassdoorUser(user=uuser,
              major=umajor,
              school=uschool)

    u.save()
    classdoorUsers.append(u)


# Create Reviews
reviews = []
for i in range(0, len(courses) - 1):
    currClass = courses[i]
    rGrade = Decimal(1)
    rStarRating = Decimal(fake.random_int(0, 500)) / 100

    for j in range(1, fake.random_int(3, 20)):
        rTitle = fake.text(25)
        rText = fake.text(200)

        review = Review(title=rTitle,
                        text=rText,
                        gradeReceived=rGrade,
                        starRating=rStarRating,
                        courseOfReview=currClass)

        review.save()
        reviews.append(review)

        currClass.reviews.add(review)
        currClass.save()

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

