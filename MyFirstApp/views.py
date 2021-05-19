from django.shortcuts import render,HttpResponse
from MyFirstApp.models import contact_cls

# Create your views here.
def index(request):
    return render(request, 'index.html',)
    # return HttpResponse("Hello world")
def services(request):
    return render(request,"service.html")
def contacts(request):
    # print(request.GET,"$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    if request.method=='POST':
        # print(request.POST,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        email= request.POST.get('email')
        password= request.POST.get('passwd')

        contact=contact_cls(email=email, password=password)
        contact.save()
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")
