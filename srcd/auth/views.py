from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model

User = get_user_model()

# Create your views here.
def login_view(request):
    username =  request.POST.get("username") or None
    password =  request.POST.get("password") or None
    
    if all([username, password]):
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'auth/login.html')


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username') or None
        password =  request.POST.get("password") or None
        email =  request.POST.get("email") or None
        # How django form validates email and user exists
        # user_exists_qs = User.objects.filter(username_iexact=username).exists()
        # email_exists_qs = User.objects.filter(email_iexact=email).exists()
        try:
            User.objects.create_user(username, email=email, password=password)
        except:
            pass
        
    
    return render(request, "auth/register.html")