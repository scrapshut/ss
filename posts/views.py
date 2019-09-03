from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from datetime import datetime
from .models import Post, Comment
from django.urls import reverse
from .forms import PostCreateForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.utils.safestring import mark_safe
import json
from django.views.generic.list import ListView
from django.contrib.auth.models import User
# Create your views here.

#
def post_list(request):
    return render(request,'posts/newsfeed.html')
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
    return render(request, 'posts/newsfeed.html', context)


def like_post(request,id):
    # id=request.POST.get('psts_id')
    # id=float(id)
    psts = get_object_or_404(Post, id=id)
    is_liked = False
    if psts.likes.filter(id=request.user.id).exists():
        psts.likes.remove(request.user)
        is_liked = False
        message = 'You disliked this'
    else:
        psts.likes.add(request.user)
        is_liked = True
        message = 'You liked this'

    # total=psts.likes.count.all()
    x=psts.likes.count()
    # x=[x.count() for x in psts.likes.all()]
    ctx = {'likes_count':x, 'message': message}

    # ctx = {'likes_count':[x.as_dict() for x in psts.likes.all()], 'message': message}
    return HttpResponse(json.dumps(ctx), content_type='application/json')

    # total=mark_safe(json.dumps(list(total), ensure_ascii=False))
    # print(total)
    # return JsonResponse({'like_count':total})

    # return HttpResponse('ok this is awesome')
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
# def UserView(request):
#     args = {'user':request.user}
#     return render(request,'posts/timeline.html')
# @login_required
def comment(request, pk):
   post= get_object_or_404(Post, pk=pk)
   pst=Post.objects.all()
   if request.method == 'POST':
       comment = CommentForm(request.POST)
       if comment.is_valid():
          comment = comment.save(commit=False)
          comment.post= post
          comment.user = request.user
          comment.save()
          # return redirect('post_detail', slug=post.slug)
   else:
       form = CommentForm()
   return render(request, 'posts/newsfeed.html', {'comment':comment})
def post_create(request,pk=''):
    print(pk)
    if request.method=='POST':
        form = PostCreateForm(request.POST,request.FILES)
        comment=CommentForm(request.POST)
        # print(comment)
        if pk:

            pos=Post.objects.get(pk=pk)
            return pos

            # print(pos)
        # comment=
        # print(form)
        if request.FILES:
            print('there is a file')
        else:
            print('no file')

        # if re
        # if form.is_valid() or comment.is_valid():
        if form:
            if form.is_valid():

                psts = form.save(commit=False)
                psts.author = request.user
                print(psts.image)
                psts.save()
                return redirect('posts:post_create')
            else:
                print("form is not valid")
        if comment:
            if comment.is_valid():
                c=comment.save(commit=False)
                comment = c
                comment.post= pos
                comment.user = request.user
                comment.save()
                return redirect('posts:post_create')

                    # return HttpResponseRedirect(reverse('post_create'))
                    # return redirect("views.post_create")
            else:
                print("something is wrong")
        # else:
        #     print("form is not valid")
    else:
        form = PostCreateForm()
        comment=CommentForm()
    pst = Post.objects.all()
    query = request.GET.get('q')
    if query:
        pst = Post.objects.filter(title=query)


    context = {
        'pst':pst,
        'form': form,
        'comment':comment


    }
    return render(request,'posts/newsfeed.html', context)


class UserAnnouncesList(ListView):
    model = Post
    template_name = 'posts/timeline.html'
    context_object_name = 'user'

    def get_queryset(self):
        # user=self.user
        return Post.objects.all().filter(owner=self.request.user)

        # return Post.objects.filter(owner=self.request.user)
# def UserView(self):
#     user=self.user
#     user = Post.objects.get(user__username=request.user.username)
#
#     # user=Post.objects.all().filter(user=user)
#     print(user)
#     context = {
#         'user':user,
#     }
#     return render(request,'posts/timeline.html', context)
