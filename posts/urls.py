"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from posts import views
from scrapshut import settings
# from . import views, settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



app_name = 'posts'
urlpatterns = [
    url(r'^$', views.post_create,name='post_create'),
    url(r'^/(?P<pk>\w+)/$', views.post_create,name='post_create'),
    # path('', views.post_create, name='post_create'),
    # url(r'^$', views.post_create, name="post_create"),
    # url(r'^$/(?P<pk>\d+)/$', views.post_create, name="post_create"),
    # path(r'$/<int:pk>/', views.post_create, name="post_create"),

    path('comment/<int:pk>/', views.comment, name='comments'),

    # url(r'^create_post/$', views.post_create, name="post_create"),
    url(r'users/(?P<pk>[0-9]+)/$', views.UserAnnouncesList.as_view(), name='user_announces_list'),

    # url(r'^user/$', views.UserView, name="user_list"),

    url(r'^like_post/(?P<id>\d+)/$',views.like_post, name="like_post"),

    url(r'^home/$', views.post_list, name="post_list"),
    url(r'^posts/(?P<id>\d+)/$',views.post_detail, name="post_detail"),
    #url(r'^posts/(?P<id>\d+)/(?P<slug>[\w-]+)/$',views.post_detail, name="post_detail"),

    # url(r'^/$', views.post_create, name="post_create"),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG: # new
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
