from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello, this is Users Home Page")
def home(request):
    return render(request, 'myapp/home.html')