from django import forms
from .models import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'content', 'book_title', 'book_author')

class UserReistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="confilm Password")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean(self):
        cleaned_date = super().clean()
        password = cleaned_date.get('password')
        password_confirm = cleaned_date.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError('password dose not match.')
        return cleaned_date
    
    
    
