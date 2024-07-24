from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterUserForm, LoginUserForm, PostForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Post

# Create your views here.
def home_blog(request):
    return render(request, 'index.html', {})

def register_blog_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have been registered! You are now logged in')
                return redirect('post:home')
        else:
            messages.warning(request, "There was an error registering. Try again!")
            return redirect('post:register')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form': form})

@login_required
def logout_blog_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('post:home')

def login_blog_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been logged in!")
                return redirect('post:home')
        else:
            messages.warning(request, "Failed to login. Try again!")
    else:
        form = LoginUserForm()
    return render(request, 'login.html', {'form': form})

@login_required
def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

@login_required
def new_post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'New post created!')
            return redirect('post:home')
    else:
        form = PostForm()
    return render(request, 'newpost.html', {'form': form})