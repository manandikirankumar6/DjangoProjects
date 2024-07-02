from django.shortcuts import render

# Create your views here.
def my_view(request):
    myName="kiran"
    favPlayer="Dhoni"
    favAnimal="Lion"
    favSubject="Python"
    d={"name":myName,"player":favPlayer,"animal":favAnimal,"subject":favSubject}
    return render(request,"Myapp/1.html",d)