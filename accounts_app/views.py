from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.

from .decorators import *
from .form import *
from .models import *

@authenticate_user
def loginPage(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.user_profile.first_login:
                user.user_profile.first_login = False
                return redirect( reverse( 'accounts:profile' ))

            group = None
            if user.groups.exists():
                group = user.groups.all()[0].name

                if group == 'teacher':
                    return redirect( reverse( 'teacher:dashboard'))

        messages.info(request, 'Username OR password is incorrect')
        return render(request, 'accounts/login_page.html')
    else:
        return render(request, 'accounts/login_page.html')

def logoutUser(request):
    logout(request)
    return redirect( reverse('accounts:login'))


@login_required(login_url='accounts:signin')
def profile( request ):

    userprofile = request.user.user_profile
    access = request.user.permission_set.all()

    context = {
        'user_profile': userprofile,
        'access': access,
    }

    return render(request, 'accounts/profile.html', context)
