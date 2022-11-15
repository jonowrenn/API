from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.

class Apiview(View):
    def get(self, request, num,):
        return HttpResponse(num ** 2)

class HelloWorldView(View):
    def get(self, request,):
        return HttpResponse('Hello world!')