from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.contrib.auth.models import User

# from django.contrib.auth.models import User
# class UserManager(BaseUserManager):
#     def create_user(self, username, email, password):
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         elif not username:
#             raise ValueError('Users must have an username')
#
#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
# class User(AbstractBaseUser):
#     GENDER_CHOICES = (
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#     )
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
#     username = models.CharField(
#         verbose_name='username',
#         max_length=30,
#         unique=True,
#     )
#     name = models.CharField(max_length=30, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     gender = models.CharField(verbose_name='gender', max_length=10, choices=GENDER_CHOICES, null=True)
#     date_of_birth = models.DateField('date of birth',blank=True, null=True)
#     avatar = models.FileField(upload_to='profile_photo', null=True)
#     quote = models.TextField(verbose_name='quote',max_length=500, blank=True, null=True)
#     contact = models.IntegerField(verbose_name='contact', blank=True, null=True)
#     objects = UserManager()
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']
#
#     def get_full_name(self):
#         return self.name
#
#     def get_short_name(self):
#         return self.name
#
#     def __str__(self):
#         return self.username
#
#     def has_perm(self, perm, obj=None):
#         return True
#
#     def has_module_perms(self, app_label):
#         return True
#
#     def get_absolute_url(self):
#         return reverse('accounts:profile', kwargs={'username': self.username})
#
#     @property
#     def is_staff(self):
#         return self.is_admin

# class Connection(models.Model):
#     follower = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='follower',null=True,blank=True)
#     following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='following')
#     date_created = models.DateTimeField(auto_now_add=True)


    # def __str__(self):
    #     return "{} : {}".format(
    #         self.follower,
    #         self.following
    #     )
# class User(AbstractUser):
#     """ Custom User Model
#         In cases where we just want to add a new field to the already existing user, subclass
#         the `AbstractUser` and add the required fields
#         Ensure to update the `settings.AUTH_USER_MODEL` value
#     """
#     followers = models.ManyToManyField("self", blank=True)
#
#     def is_following(self, user):
#         return user in self.followers.all()
#
# class UserLink(models.Model):
#     """
#     A single directed edge in the social graph.  Usually represented as the
#     verb "follows".
#
#     """
#     from_user = models.ForeignKey(User, related_name='following_links',on_delete=models.CASCADE)
#     to_user = models.ForeignKey(User, related_name='follower_links',on_delete=models.CASCADE)
#     # date_added = models.DateTimeField(default=datetime.now)
#
#     def __unicode__(self):
#         return u"%s is following %s" % (self.from_user.username,
#             self.to_user.username)
#
#     def save(self, **kwargs):
#         """
#         A mostly-generic save method, except that it validates that the user
#         is not attempting to follow themselves.
#         """
#         if self.from_user == self.to_user:
#             raise ValueError("Cannot follow yourself.")
#         super(UserLink, self).save(**kwargs)
#
#     class Meta:
#         unique_together = (('to_user', 'from_user'),)
#
#
# class UserProfile(models.Model):
#     """ Profile data of user """
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE,
#                                 related_name='profile',
#                                 verbose_name='other Details')
#     picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
#     website = models.URLField(blank=True)
#     bio = models.TextField(blank=True)
#     phone = models.CharField(max_length=11, blank=True)
#     address = models.CharField(max_length=100, blank=True)
#
#     def __str__(self):
#         return self.user.username
#
#
# @receiver(post_save, sender=User)
# def create_profile(sender, **kwargs):
#     """ Create a profile anytime a new user is created """
#     if kwargs['created']:
#         user_profile = UserProfile.objects.get_or_create(
#                                     user=kwargs['instance']
#                                     )

class User(AbstractUser):

    followers = models.ManyToManyField("self", blank=True)
    following = models.ManyToManyField("self",blank=True)

    def is_following(self, user):
        return user in self.followers.all()
    def is_followed(self,user):
        return user in self.following.all()



class UserProfile(models.Model):
    """ Profile data of user """

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile',
                                verbose_name='other Details')
    picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    timeline = models.ImageField(upload_to='timeline_pictures', blank=True, null=True)

    website = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=11, blank=True)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    """ Create a profile anytime a new user is created """
    if kwargs['created']:
        user_profile = UserProfile.objects.get_or_create(
                                    user=kwargs['instance']
                                    )
