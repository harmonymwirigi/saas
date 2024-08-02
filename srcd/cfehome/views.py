import pathlib
from django.shortcuts import render
from django.http import HttpResponse

from visits.models import PageVisit

def home_page_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    
    my_title = "My page"
    
    context = {
        "page_title": my_title,
        "queryset_count": queryset.count()
    }
    
    html_template = "home.html"
    PageVisit.objects.create(path = request.path)
    
    return render(request, html_template, context)