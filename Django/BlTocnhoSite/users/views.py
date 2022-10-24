from django.shortcuts import render
from users.forms import RegisterForm, LoginForm, PasswordRecoveryForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib import auth
from django.contrib.auth import update_session_auth_hash


def register(request):

    if request.method == 'POST':
        register_form = RegisterForm(request.POST or None)

        if register_form.is_valid() and register_form.data['password'] == register_form.data['corfim_password']:
            register_form.save()
            return HttpResponseRedirect(reverse_lazy('login'))
        else:
            return HttpResponse(register_form.errors)

    else:
        return render(request, 'bootstrap_main/register.html')


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse_lazy('home'))
        else:
            return HttpResponse(login_form.errors)
    else:
        return render(request, 'bootstrap_main/login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse_lazy('home'))


def user_card(request):
    if request.method == 'POST':
        edit_form = LoginForm(request.POST, request.FILES,
                              instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse_lazy('user'))
    else:
        edit_form = LoginForm(instance=request.user)
        return render(request, 'bootstrap_main/user_card.html')


def password(request):
    if request.method == 'POST':
        form = PasswordRecoveryForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        return render(request, 'bootstrap_main/password.html')
