from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader

from searchEngine.utils import engine


# Create your views here.
def index(request):
    if 'q' in request.GET:
        sentences_info = engine(request.GET['q'], "text.txt")
        context = {"sentences": sentences_info}
        return render(request, "index.html", context=context)
    else:
        return render(request, "index.html")
