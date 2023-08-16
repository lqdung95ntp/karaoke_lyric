from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_user(request):
    logout(request)
    if request.method == "POST":
        if 'login_username_txt' in request.POST:
            # login mode
            username = request.POST["login_username_txt"]
            password = request.POST["login_pass_txt"]
            print(username, password)
            # check if password is existed
            is_user_existed = User.objects.filter(username=username).exists()
            # check if user/password is correct
            if not is_user_existed:
                message = 'User {} is not existed!'.format(username)
                return render(request, 'login.html', context={'message': message})

            user = authenticate(request, username=username, password=password)
            if user is not None:
                request.session.set_expiry(1209600)  # 2 weeks
                login(request, user)
                # Redirect to a success page.
                return redirect('personal')
            else:
                # Return an 'invalid login' error message.
                message = 'Password is not correct, please check again!'
                return render(request, 'login.html', context={'message': message, 'username': username})
        
    return render(request, 'login.html')

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')

def register_user(request):
    logout(request)
    if request.method == "POST":
        if "reg_name_txt" in request.POST:
            name = request.POST["reg_name_txt"]
            username = request.POST["reg_username_txt"]
            email = request.POST["reg_email_txt"]
            password = request.POST["reg_pass_txt"]
            password2 = request.POST["reg_pass2_txt"]

            is_user_existed = User.objects.filter(username=username).exists()
            if is_user_existed:
                return render(request, 'register.html',
                              context={'message': 'User {} is existed!'.format(username)})

            if password != password2:
                return render(request, 'register.html',
                              context={'message': 'Passwords is not the same!'})

            first_name = name.split(' ')[0]
            last_name = name.split(' ')[-1]
            User.objects.create_user(username=username, email=email, password=password,
                                    first_name=first_name, last_name=last_name)
            return redirect('login')
    return render(request, 'register.html')