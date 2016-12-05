from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import Http404
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    if 'GET' == request.method:
        if request.user.is_authenticated():
            return redirect('/')
        else:
            return render(request, 'user/login.html')

    elif 'POST' == request.method:
        try:
            user = User.objects.get(email=request.POST['email'])
            auth_user = authenticate(username=user.username, password=request.POST['password'])

            if auth_user is not None:
                login(request, auth_user)
                return redirect('/')
            else:
                error = 'wrong email/password combination'
                return render(request, 'user/login.html', {'error_message': error})

        except User.DoesNotExist as e:
            return render(request, 'user/login.html', {'error_message': e})

    return Http404


def user_logout(request):
    logout(request)
    return redirect('/')


def sign_up(request):
    if 'GET' == request.method:
        if not request.user.is_authenticated():
            return render(request, 'user/register.html')
        else:
            return redirect('/')

    elif 'POST' == request.method:
        try:
            user = User.objects.create_user(
                    email=request.POST['email'],
                    username=request.POST['userName'],
                    password=request.POST['password']
                )
            user.is_staff = False
            user.save()
        except IntegrityError as e:
            error = e
            return render(request, 'user/register.html', {'error_message': error})
        else:
            return redirect('/')
