import re
from django.shortcuts import render
from classdoor.models import Course, Teacher, Review, University, User, Subject
from django.db.models.query import EmptyQuerySet
from django.forms import ModelForm
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "index.html")

def classpage(request, id):
    # Get the individual course by id from url
    course = Course.objects.get(pk=id)

    courseData = {}
    courseData["class"] = course
    courseData["name"] = course.name
    courseData["description"] = course.description
    courseData["teacher"] = course.teacher
    courseData["star_rating"] = course.starRating
    courseData["reviews"] = course.reviews
    courseData["average_grade"] = course.averageGrade
    courseData["subject"] = course.subject
    courseData["university_name"] = course.university_name

    # Get all the reviews for the course
    reviews = course.reviews.all()
    reviewClass = '/review/' + str(id)

    reviewList = []

    # Get the information about all the individual reviews in the list
    for rdata in reviews:
        reviewData = {}
        reviewData["review"] = rdata
        reviewData["title"] = rdata.title
        reviewData["text"] = rdata.text
        reviewData["star_rating"] = rdata.starRating
        reviewData["grade_received"] = rdata.gradeReceived
        reviewData["date"] = rdata.date
        reviewData["tags"] = rdata.tags
        reviewData["author"] = rdata.author

        reviewList.append(reviewData)

    # Add to course information and the list of reviews to the page context
    context = {
        "class": courseData,
        "review_list": reviewList,
        "review_class_url": reviewClass
    }

    return render(request, "class.html", context=context)

def feed(request):
    context = {}

    courses = Course.objects.all()
    coursesArr = []

    for course in courses:
        courseData = {}

        numIndex = re.search("\d", course.name)

        courseData["class"] = course
        courseData["subject"] = course.name[0: numIndex.start()]
        courseData["number"] = course.name[numIndex.start(): len(course.name)]
        courseData["description"] = course.description
        courseData["star_rating"] = course.starRating

        review = course.reviews.all().first()

        if review:
            courseData["featured_title"] = review.title
            courseData["featured_text"] = review.text

        coursesArr.append(courseData)

    context["course_data"] = coursesArr

    return render(request, "feed.html", context=context)

def login(request):
    return render(request, "login.html")

def profile(request):
	courses = Course.objects.all()[2:5]
	reviews = Review.objects.all()[2:5]
	
	context = {"reviews": reviews, "courses": courses}
	return render(request, "profile.html", context=context)

def review(request, id):

    course_object = Course.objects.get(pk=id)
    course_name = course_object.name

    form = WriteReviewForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():

        #Query database and add new review for a specific class instance given by the id passed as parameter

        course_instance.starRating = form.cleaned_data['starRating']
        course_instance.gradeReceived = form.cleaned_data['gradeReceived']
        course_instance.title = form.cleaned_data['title']
        course_instance.text = form.cleaned_data['text']
        course_instance.save()

        # redirect to class page:
        #return HttpResponseRedirect(reverse('course-page', args = "id") )
        #look up reverse() method Django
        #Appears to involve defining shortcuts in project urls.py
    else:
        #Handle case it isn't a post? If you're writing a review it should be writing to the database
        #There shouldn't be a default form...



    context = {
        "course_name": course_name,
        "this_course": course_object,
        "WriteReviewForm": write_review_form,

    }
    return render(request, "WriteReviewTemplate.html", context = context)
    #NEED TO CHANGE TEMPLATE TO ACCOMODATE DJANGO FORMS

#@permission_required('catalog.can_mark_returned')
#Need to be logged in -> else redirect to login page
class WriteReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['starRating', 'gradeReceived', 'title', 'text']
        help_texts = {
            'title': _('An awesome title for this review!'),
            'text':_('Tell us about your experience in this cass')
        }