from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello World</h1>")