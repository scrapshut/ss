from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    """ Custom User Model
        In cases where we just want to add a new field to the already existing user, subclass
        the `AbstractUser` and add the required fields
        Ensure to update the `settings.AUTH_USER_MODEL` value
    """
    followers = models.ManyToManyField("self", blank=True)

    def is_following(self, user):
        return user in self.followers.all()

class UserLink(models.Model):
    """
    A single directed edge in the social graph.  Usually represented as the
    verb "follows".

    """
    from_user = models.ForeignKey(User, related_name='following_links',on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='follower_links',on_delete=models.CASCADE)
    # date_added = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return u"%s is following %s" % (self.from_user.username,
            self.to_user.username)

    def save(self, **kwargs):
        """
        A mostly-generic save method, except that it validates that the user
        is not attempting to follow themselves.
        """
        if self.from_user == self.to_user:
            raise ValueError("Cannot follow yourself.")
        super(UserLink, self).save(**kwargs)

    class Meta:
        unique_together = (('to_user', 'from_user'),)


class UserProfile(models.Model):
    """ Profile data of user """

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile',
                                verbose_name='other Details')
    picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
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
