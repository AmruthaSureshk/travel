from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import team

# Create your views here.
def demo(request):
    # name="India"
    # return render(request,"home.html",{'obj':name})

    obj=place.objects.all()
    var=team.objects.all()
    return render(request,"index.html",{'result':obj,'op':var})

# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return HttpResponse("Contact details")

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})


