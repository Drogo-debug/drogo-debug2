from django.shortcuts import render

# Create your views here.
def signinpage(request):
    return render(request,"register.html")