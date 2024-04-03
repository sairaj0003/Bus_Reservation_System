from django.contrib.auth import authenticate, alogin, alogout, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth

from .models import Users
# Views
def home(request):
    if request.user.is_authenticated:
        return render(request, 'success.html')
    return render(request, 'login_user.html')

def login_user(request):
    msg = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            msg["error"] = "Invalid Email or Password!"
            return render(request, 'login_user.html', {'msg': msg})
        return redirect("home")
    return render(request, 'login_user.html', {'msg': msg})


def register(request):
    msg = {}
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST['username']
        password = request.POST.get('password')
        re_enter_password = request.POST.get('re_enter_password')

        # if User.objects.filter(username=username).exists():
        #     messages.error(request, "Username is already taken. Please try another one !")
        #     return redirect("/")

        # if len(username) > 15:
        #     messages.error(request, "Username must be less than 15 characters")
        #     return redirect("/")
        
        # if not username.isalnum():
        #     messages.error(request, "Username should only contain Letters and Numbers.")

        # if pass1 != pass2:
        #     messages.error(request, "Password Do not Match. Please Sign Up Again")
        #     return redirect("/")


            
        if password != re_enter_password:
            msg["error"] = "Passwords does not matched!"
            return render(request, 'register.html', {'msg': msg})
        else:
            try:
                myuser = User.objects.create_user(username, email, password)
                myuser.first_name = first_name
                myuser.last_name = last_name
                myuser.save()
                msg["success"] = "You are successfully Registered"
                return render(request, 'login_user.html', {'msg': msg})
                # return redirect('login')
            except Exception as e:
                msg["error"] = e
            # msg["error"] = "Provide valid credentials!\nFirst Name should be less than 100 characters\nLast Name should be less than 100 characters\nPassword should be less than 30 characters"
                return render(request, 'register.html', {'msg': msg})
    else:
        return render(request, 'register.html', {'msg': msg})

def logout_user(request):
    logout(request)
    # return render(request, "login_user.html")
    return redirect("login_user")

'''
def register(request):
    msg = {}
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_enter_password = request.POST.get('re_enter_password')
        if password != re_enter_password:
            msg["error"] = "Passwords does not matched!"
            return render(request, 'register.html', {'msg': msg})
        else:
            try:
                Users.objects.create(first_name=first_name, last_name=last_name, email=email, password=password, )
                msg["success"] = "You are successfully Registered"
                return render(request, 'login.html', {'msg': msg})
                # return redirect('login')
            except Exception as e:
                msg["error"] = e
            # msg["error"] = "Provide valid credentials!\nFirst Name should be less than 100 characters\nLast Name should be less than 100 characters\nPassword should be less than 30 characters"
                return render(request, 'register.html', {'msg': msg})
    else:
        return render(request, 'register.html', {'msg': msg})


def login(request):
    msg = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = get_object_or_404(Users, email=email, password=password)
            if user is not None:
                alogin(request, user)
            return render(request, 'success.html')
        except Exception:
            msg["error"] = "Invalid Email or Password!"
            return render(request, 'login.html', {'msg': msg})
    return render(request, 'login.html', {'msg': msg})

def logout(request):
    alogout(request)
    return render(request, "logout.html")
'''

@login_required(login_url="login_user")
def success(request):
    return render(request, 'success.html')

