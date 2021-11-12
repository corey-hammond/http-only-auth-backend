from django.urls import path
from django.urls.resolvers import URLPattern
from .views import RegisterView, LoadUserView

urlpatterns = [
  path('register', RegisterView.as_view()),
  path('user', LoadUserView.as_view()),
]