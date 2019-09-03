from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
from django.db.models import CharField
from django.conf import settings


# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     body = models.TextField()
#     pub_date = models.DateTimeField()
#     author = models.ForeignKey(User,on_delete=models.CASCADE)
#     votes_total = models.IntegerField(default=1)
#     likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True)
#
#
#     def pub_date_pretty(self):
#         return self.pub_date.strftime('%b %e %Y')
#     def __str__(self):
#         return self.title
#
#     def total_likes(self):
#         return self.likes.count()
#
#     def get_absolute_url(self):
#         return reverse(
#             "posts:post_detail",
#             kwargs={
#                 "id": self.id,
#                 # "slug": self.slug
#
#             }
#         )
# class PublishedManager(models.Manager):
#     def get_queryset(self):
#         return super(PublishedManager, self).get_queryset().filter(status="published")


class Post(models.Model):
#     objects=models.Manager()
#     published = PublishedManager()
#     STATUS_CHOICES = (
#         ('draft', 'Draft'),
#         ('published', 'Published')
#     )
    title = models.CharField(max_length=200)
    body = models.TextField()
    # comment=models.ManyToManyField(Comment)
    image=models.ImageField(null=True,upload_to="gallery",blank=True)
    # pub_date = models.DateTimeField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True)
    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Published')
#
    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse(
            "posts:post_detail",
            kwargs={
                "id": self.id,
                # "slug": self.slug

            }
        )
    #
    # def get_absolute_url(self):
    #     return reverse("posts:post_detail", args=[self.id,self.slug])

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user',blank=True)
    content = models.TextField(max_length=160, default="")
    post=models.ForeignKey(Post,on_delete=models.CASCADE,null=True,related_name='post')
    # timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(str(self.user.username))
@receiver(pre_save, sender=Post)
def pre_save_slug(sender, **kwargs):
    slug=slugify(kwargs['instance'].title)
    kwargs['instance'].slug=slug
