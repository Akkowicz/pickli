from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import PostForm
from .models import Post

# Create your views here.


def index_wiki(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            post_name = form.cleaned_data['post_name']
            content = form.cleaned_data['content']
            p = Post(title=post_name, content=content, date_added=datetime.now())
            p.save()
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()
    return render(request, "index.html", {'form': form})
