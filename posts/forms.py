from .models import Post, Comment
from django import forms
from django.contrib.auth.models import User



class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        # fields = "__all__"
        fields=('title','body','image')
        widgets = {
            'title': forms.TextInput(attrs={
                'id': 'exampleFormControlInput1',
                'required': True,
                'placeholder': 'Say something...'
            }),
            'body': forms.TextInput(attrs={
                'id': 'exampleFormControlTextarea1',
                'required': True,
                'placeholder': 'Say something...'
            }),
        }
        # fields=['title','body']

# class UserLoginForm(forms.Form):
#     username=forms.CharField(label="")
#     password=forms.CharField(label="", widget=forms.PasswordInput)
#
#
# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter the Password'}))
#     confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
#
#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#         )
#
#     def clean_confirm_password(self):
#         password=self.cleaned_data.get('password')
#         confirm_password=self.cleaned_data.get('confirm_password')
#         if password != confirm_password:
#             raise forms.ValidationError("Passwords mismatch!")
#
#         return confirm_password

# class
class CommentForm(forms.ModelForm):
    # content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Its easy to pass comment, but yeah you can!', 'rows': '2', 'cols': '50'}))
    class Meta:
        model = Comment
        fields = ('user','content')
