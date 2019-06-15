from django.shortcuts import render
from .forms import PostCreateForm, UserLoginForm, UserRegistrationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from posts.models import Post
from django.urls import reverse
from .forms import PostCreateForm, UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def user_login(request):
    if request.method=='POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('posts:post_list'))
                else:
                    return HttpResponse("User is inactive")
            else:
                return HttpResponse("User is None")
    else:
        form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('posts:post_list')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('post:post_list')
    else:
        form=UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/register.html', context)\
