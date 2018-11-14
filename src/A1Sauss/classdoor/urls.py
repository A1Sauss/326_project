from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("class/", RedirectView.as_view(url='/feed/',permanent=True)),
    path("class/<int:id>", views.classpage, name="class-detail"),
    path("feed/", views.feed, name="feed"),
    path("login/", views.login, name="login"),
    path("profile/", views.profile, name="profile"),
    path("profile/<int:id>", views.profile, name="profile"),
    path("review/", RedirectView.as_view(url='/feed/',permanent=True)),
    path("review/<int:id>", views.review, name="review-detail")
]