from django.shortcuts import render

# Create your views here.
def template1(request):
    my_data={"name":"Adithya M S"}
    return render(request,'home/template1.html',context=my_data)

def template2(request):
    return render(request,'home/template2.html',context={})

def template3(request):
    return render(request,'home/template3.html',context={})

def template4(request):
    return render(request,'home/template4.html',context={})