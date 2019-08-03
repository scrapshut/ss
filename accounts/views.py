from django.shortcuts import render
from .forms import  UserRegistrationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from posts.models import Post
from django.urls import reverse
from .forms import  UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
############
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import UserLoginForm
####follow
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.views import LoginView

from .forms import ProfileForm
from .models import UserProfile
from django.contrib.auth import get_user_model
User = get_user_model()


from .models import UserLink
from .utils import (get_next, get_people_user_follows,
                             get_people_following_user, get_mutual_followers)

FRIEND_FUNCTION_MAP = {
    'followers': get_people_following_user,
    'following': get_people_user_follows,
    'mutual': get_mutual_followers,
}


def friend_list(request, list_type, username):
    """
    Renders a list of friends, as returned by the function retrieved from the
    ``FRIEND_FUNCTION_MAP``, given the user specified by the username in the
    URL.

    """
    user = get_object_or_404(User, username=username)
    context = {
        'list_type': list_type,
        'friends': FRIEND_FUNCTION_MAP[list_type](user),
    }
    return render_to_response(
        'followers/friend_list.html',
        context,
        context_instance=RequestContext(request)
    )


@login_required
def follow(request, username):
    """
    Adds a "following" edge from the authenticated user to the user specified
    by the username in the URL.

    """
    user = get_object_or_404(User, username=username)
    ul, created = UserLink.objects.get_or_create(from_user=request.user,
        to_user=user)
    next = get_next(request)
    if next and next != request.path:
        # request.user.message_set.create(
        #     message=_('You are now following %s') % user.username)
        return HttpResponseRedirect(next)
    context = {
        'other_user': user,
        'created': created,
    }
    return render_to_response(
        'followers/followed.html',
        context,
        context_instance=RequestContext(request)
    )


@login_required
def unfollow(request, username):
    """
    Removes a "following" edge from the authenticated user to the user
    specified by the username in the URL.

    """
    user = get_object_or_404(User, username=username)
    try:
        ul = UserLink.objects.get(from_user=request.user, to_user=user)
        ul.delete()
        deleted = True
    except UserLink.DoesNotExist:
        deleted = False
    next = get_next(request)
    if next and next != request.path:
        # request.user.message_set.create(
        #    message=_('You are no longer following %s') % user.username)

        return HttpResponseRedirect(next)
    context = {
        'other_user': user,
        'deleted': deleted,
    }
    return render_to_response(
        'followers/unfollowed.html',
        context,
        context_instance=RequestContext(request)
    )
def user_login(request):
    if request.method=='POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user_name = request.POST['username']
            pass_word = request.POST['password']
            user = authenticate(username=user_name, password=pass_word)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('posts:post_create'))
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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'posts/login.html', {'form': form})
def user_logout(request):
    logout(request)
    return redirect('posts:post_create')

#
# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST or None)
#         if form.is_valid():
#             new_user = form.save(commit=False)
#             new_user.set_password(form.cleaned_data['password'])
#             new_user.save()
#             return redirect('post:post_list')
#     else:
#         form=UserRegistrationForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'posts/register.html', context)
# @csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('posts/acc_active_email.html', {
                'user':user, 'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            # Sending activation link in terminal
            # user.email_user(subject, message)
            mail_subject = 'Activate your ScrapShut account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            #return HttpResponse('Please confirm your email address to complete the registration.')
            return render(request, 'posts/acc_active_sent.html')
    else:
        form = UserRegistrationForm()
    return render(request,'posts/login.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        return render(request, 'posts/confirmed.html')
    else:

        return HttpResponse('Activation link is invalid!')




@login_required
def profile(request, username):
    """ view profile of user with username """

    user = User.objects.get(username=username)
    # check if current_user is already following the user
    is_following = request.user.is_following(user)
    return render(request, 'accounts/users_profile.html', {'user': user, 'is_following': is_following})


@login_required
def edit_profile(request):
    """ edit profile of user """

    if request.method == "POST":
        # instance kwargs passed in sets the user on the modelForm
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view-profile', args=(request.user.username, )))
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})


@login_required
def followers(request):
    """ Return the lists of friends user is  following and not """

    # get users followed by the current_user
    users_followed = request.user.followers.all()

    # get_users not followed and exclude current_user from the list
    unfollowed_users = User.objects.exclude(id__in=users_followed).exclude(id=request.user.id)
    return render(request, 'accounts/followers.html', {'users_followed': users_followed, 'unfollowed_users': unfollowed_users})


@login_required
def follow(request, username):
    """ Add user with username to current user's following list """

    request.user.followers.add(User.objects.get(username=username))
    return redirect('accounts:followers')


def unfollow(request, username):
    """ Remove username from user's following list """

    request.user.followers.remove(User.objects.get(username=username))
    return redirect('accounts:followers')
