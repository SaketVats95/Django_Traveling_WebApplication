from django.shortcuts import render
from django.http import HttpResponse

def Hello(request):
    #text="""<h1>Welcome Saket Vats to My Application</h1>"""
    name="Saket"
    sentence=request.GET.get("sentence")
    word=request.GET.get("word")
    count="zero"

    return render(request,"hello.html",{'name':name,'word':word,'count':count})

def ShowMessage(request,articleID='24'):
    text="Article ID::: %s" %articleID
    return HttpResponse(text)

def showAdd(request):
    num1= request.POST.get("word")
    return HttpResponse(num1)

# Create your views here.
