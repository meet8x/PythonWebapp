from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hi(request):
    return render(request,'mainwebsite/hi.html')
def about(request):
    return render(request,'mainwebsite/about.html')
def gallary(request):
    return render(request,'mainwebsite/gallary.html')
def contact(request):
    return render(request, 'mainwebsite/index.html')