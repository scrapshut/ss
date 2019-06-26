from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import Post, Comment
from django.urls import reverse
from .forms import PostCreateForm, UserLoginForm, UserRegistrationForm, CommentForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def post_list(request):
    pst = Post.published.all()
    query = request.GET.get('q')
    if query:
        pst = Post.published.filter(title=query)
    context = {
        'pst': pst,
    }
    return render(request, 'posts/post_list.html', context)

def post_detail(request, id):
    psts = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(psts=psts, reply=None).order_by('-id')
    is_liked = False
    if psts.likes.filter(id=request.user.id).exists():
        is_liked = True

    if request.method=='POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs=None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)

            comment = Comment.objects.create(psts=psts, user=request.user, content=content, reply=comment_qs)
            comment.save()
            return HttpResponseRedirect(psts.get_absolute_url())
    else:
        comment_form=CommentForm()


    context = {
        'psts': psts,
        'is_liked': is_liked,
        'total_likes': psts.total_likes(),
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'posts/post_detail.html', context)


def like_post(request,id):
    # id=request.POST.get('psts_id')
    # id=float(id)
    psts = get_object_or_404(Post, id=id)
    is_liked = False
    if psts.likes.filter(id=request.user.id).exists():
        psts.likes.remove(request.user)
        is_liked = False
    else:
        psts.likes.add(request.user)
        is_liked = True
    return HttpResponse('ok this is awesome')
    # return HttpResponseRedirect()


def post_create(request):
    if request.method=='POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            psts = form.save(commit=False)
            psts.author = request.user
            psts.save()
    else:
        form = PostCreateForm()

    context = {
        'form': form,
    }
    return render(request, 'posts/post_create.html', context)
