from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homefn(request):
    print("hello")
    # return HttpResponse("hi")
    return render(request,'index.html')