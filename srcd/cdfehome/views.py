import pathlib
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from visits.models import PageVisit

LOGIN_URL = settings.LOGIN_URL

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

VALID_CODE = 'abc123'

def pw_protected_view(request, *args, **kwargs):
    is_allowed = request.session.get('protected_page_allowed') or 0
    print(request.session.get('protected_page_allowed'), type)
    if request.method == "POST":
        user_pw_sent = request.POST.get('code') or None
        if user_pw_sent == VALID_CODE:
            is_allowed =1
            request.session['protected_page_allowed'] = is_allowed
    
    if is_allowed:
        return render(request, "protected/view.html", {})
    
    return render(request, "protected/entry.html", {})

@login_required(login_url=LOGIN_URL)
def user_only_view(request, *args, **kwargs):
    
    return render(request, "protected/user-only.html", {})

@staff_member_required(login_url=LOGIN_URL)
def staff_only_view(request, *args, **kwargs):
    
    return render(request, "protected/user-only.html", {})