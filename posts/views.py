from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import Post, Comment
from django.urls import reverse
from .forms import PostCreateForm, CommentForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def post_list(request):
    return render(request,'newsfeed.html')
    # pst = Post.published.all()
    # query = request.GET.get('q')
    # if query:
    #     pst = Post.published.filter(title=query)
    # context = {
    #     'pst': pst,
    # }
    # return render(request, 'posts/post_list.html', context)

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

# def post_create(request):
#     if request.method == 'POST':
#         if request.POST['title'] and request.POST['body']:
#             post = Post()
#
#             post.title = request.POST['title']
#             # if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
#             #     post.url = request.POST['url']
#             # else:
#             #     post.url = 'http://' + request.POST['url']
#             # post.pub_date = timezone.datetime.now()
#             post.author = request.user
#             post.save()
#             # return redirect('home')
#         else:
#             return render(request, 'newsfeed.html', {'error':'ERROR: You must include a title and a URL to create a post.'})
#     else:
#         return render(request, 'newsfeed.html')
def post_create(request):
    if request.method=='POST':
        form = PostCreateForm(request.POST)
        print(form)
        if form.is_valid():
            psts = form.save(commit=False)
            psts.author = request.user
            psts.save()
        else:
            print("form is not valid")
    else:
        form = PostCreateForm()
    pst = Post.objects.all()
    query = request.GET.get('q')
    if query:
        pst = Post.objects.filter(title=query)


    context = {
        'pst':pst,
        'form': form,
    }
    return render(request,'posts/newsfeed.html', context)

def index(request):
    return render(request,'index.html')
