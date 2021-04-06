from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_wiki(request):
    html = "<html><body>Index page.</body></html>"
    return HttpResponse(html)