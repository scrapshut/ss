from posts.models import Post
from django import forms
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms.models import inlineformset_factory

from .models import UserProfile

User = get_user_model()

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'body',
            'status',
        )


class UserLoginForm(forms.Form):
    username=forms.CharField(label="",widget=forms.TextInput(attrs={'type': 'text', 'id':'register-form-name', 'name':'register-form-name', 'value':"", 'class':'form-control'}))
    password=forms.CharField(label="",widget=forms.TextInput(attrs={'type': 'password', 'id':'register-form-name', 'name':'register-form-name', 'value':"", 'class':'form-control'}))

#
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter the Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = (
            'first_name',
                      'last_name',
                      'username',
                      'email',
                      'password1',
                      'password2',
        )

    def clean_confirm_password(self):
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords mismatch!")

        return confirm_password
# class RegistrationForm(UserCreationForm):
#     """ Extending the UserCreationForm to specify custom rendering """
#
#     email = forms.EmailField(required=True)
#     password1 = forms.CharField(label='Password',
#                                 widget=forms.PasswordInput,
#                                 required=True,
#                                 )
#     password2 = forms.CharField(label='Confirm Password',
#                                 widget=forms.PasswordInput,
#                                 required=True,
#                                 )
#     username = forms.CharField(required=True)
#
#     class Meta:
#         model = User
#         fields = ('first_name',
#                   'last_name',
#                   'username',
#                   'email',
#                   'password1',
#                   'password2',
#                   )
#
#
#

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields=('picture', 'bio', 'phone', 'website', 'address')
