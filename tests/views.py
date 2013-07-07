# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def test_formsubmit( request ):
    if request.method == "POST":
        for k, v in request.POST:
            print "%s%s" % (k, v)
    return render("tests/test_formsubmit.html", request, {})


def hello( request ):
    return HttpResponse("OK")
