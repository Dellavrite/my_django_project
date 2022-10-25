from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader

from searchEngine.utils import engine


# Create your views here.
def index(request):
    if 'q' in request.GET:
        posts = engine(request.GET['q'])
        context = {"posts": posts}
        return render(request, "result.html", context=context)
    else:
        return render(request, "index.html")
