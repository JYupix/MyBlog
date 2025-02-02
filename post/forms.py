from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Post

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    email = forms.EmailField(required=True, label="Email", widget=forms.EmailInput(attrs={
        'class': 'form-control'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'class': 'form-control'}))
    password2 = forms.CharField(label=" Confirm Password", widget=forms.PasswordInput(attrs={
        'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class PostForm(forms.ModelForm):
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label="Content", widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ['title', 'content']