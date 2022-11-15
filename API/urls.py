from django.urls import path

from API.views import Apiview, HelloWorldView

urlpatterns = [
    path('<int:num>', Apiview.as_view()),
    path('', HelloWorldView.as_view()),
    ]