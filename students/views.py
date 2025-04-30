from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def students(request):
    students = [
        {'id': 1, 'Name':'Jhon Doe'}
    ]
    return HttpResponse(students)
