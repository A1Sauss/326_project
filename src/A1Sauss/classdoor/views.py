import re
<<<<<<< HEAD
from django.shortcuts import render, redirect
=======
#import operator
from django.shortcuts import render
>>>>>>> zz-3
from classdoor.models import Course, Teacher, Review, University, ClassdoorUser, Subject
from django.db.models.query import EmptyQuerySet
#Form Imports
from django.forms import ModelForm
from django import forms
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from django.contrib.auth.forms import UserChangeForm
from classdoor.forms import EditProfileForm
#from django.contrib.auth.mixins import LoginRequiredMixin
=======
from django.http import HttpResponse
#from django.db.models import Q
>>>>>>> zz-3

# Create your views here.
def index(request):
    return render(request, "index.html")

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            courses = Course.objects.filter(name=q)
            return render(request, 'search_result.html', {'courses': courses, 'query':q})
    return render(request, 'search_result.html', {'error':error})

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

@login_required
def profile(request):
	courses = Course.objects.all()[2:5]
	cdoorUser = ClassdoorUser.objects.get(user=request.user)
	reviews = Review.objects.filter(author=cdoorUser)
	
	context = {"reviews": reviews, "courses": courses, "user": request.user}
	
	return render(request, "profile.html", context=context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'profile_edit.html', args)
	
@login_required
def review(request, id):

    course_object = Course.objects.get(pk=id)
    course_name = course_object.name

    form = WriteReviewForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():

            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            starRating = form.cleaned_data['starRating']
            gradeReceived = form.cleaned_data['gradeReceived']
            date = datetime.date.today()
            tags = form.cleaned_data['tags']
            courseOfReview = course_object
            author = ClassdoorUser.objects.get(user=request.user)
            

            new_review = Review.objects.create(
                title = title,
                text = text,
                starRating = starRating,
                gradeReceived = gradeReceived,
                date = date,
                tags = tags,
                courseOfReview = courseOfReview,
                author = author,
                )


            new_review.save()
            course_object.reviews.add(new_review)

            # new_review.save()
            # reviews = Review.objects.all()
            # for r in reviews:
            #     print(r.title)
                #Review I added isn't showing up, not sure why

        # redirect to class page:
            return HttpResponseRedirect(course_object.get_absolute_url())



        #else:
        #Handle case it isn't a post? There shouldn't really be default form

    context = {
        "course_name": course_name,
        "this_course": course_object,
        "form": form,
    }

    return render(request, "WriteReviewTemplate.html", context = context)

<<<<<<< HEAD
#@permission_required('catalog.can_mark_returned')
#Need to be logged in -> else redirect to login page
class WriteReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['starRating', 'gradeReceived', 'title', 'text', 'tags']
        #Maybe set text required for some forms
        #labels = {'gradeReceived': ('What grade did you recieve in this class?')}

        widgets ={
            'title':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'An awesome title for this review!'}),
            'text':forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell us about your experience in this class'}),
            'starRating': forms.Select(attrs={'class': 'form-control'}),
            'gradeReceived': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.CheckboxSelectMultiple#(attrs={'class': 'custom-control custom-checkbox custom-control-inline'})
        }
        required ={
            'gradeReceived': False,
            'tags': False
        }
<<<<<<< HEAD
<<<<<<< HEAD
=======
#def search(request):
    #return render(request, 'search.html')
    #if 'q' in request.GET:
#        message = 'You searched for: %r' % request.GET['q']
#    else:
#        message = 'You submitted an empty form.'
#    return HttpResponse(message)
>>>>>>> zz-3
=======
>>>>>>> 970837e3d1d2bc8f1fd31d477b84cc458208b66d
=======
>>>>>>> 970837e3d1d2bc8f1fd31d477b84cc458208b66d
