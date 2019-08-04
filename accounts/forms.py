from posts.models import Post
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

from django.contrib.auth import authenticate, login, logout, get_user_model

from .models import User
# class PostCreateForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = (
#             'title',
#             'body',
#             # 'status',
#         )

# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     def clean(self, *args, **kwargs):
#         username = self.cleaned_data.get("username")
#         password = self.cleaned_data.get("password")
#         if username and password:
#             user = authenticate(username=username, password=password)
#             if not user:
#                 raise forms.ValidationError("User does not exist.")
#             if not user.is_active:
#                 raise forms.ValidationError("User is no longer active.")
#         return super(LoginForm, self).clean(*args, **kwargs)
class UserLoginForm(forms.Form):
    username=forms.CharField(label="",widget=forms.TextInput(attrs={'type': 'text', 'id':'register-form-name', 'name':'register-form-name', 'value':"", 'class':'form-control','placeholder': 'Username'}))
    password=forms.CharField(label="",widget=forms.TextInput(attrs={'type': 'password', 'id':'register-form-name', 'name':'register-form-name', 'value':"", 'class':'form-control','placeholder': 'Enter the Password'}))


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter the Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )

    def clean_confirm_password(self):
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords mismatch!")

        return confirm_password


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields=('picture', 'bio', 'phone', 'website', 'address')
