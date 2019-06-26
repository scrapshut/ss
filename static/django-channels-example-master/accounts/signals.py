from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User
from django.template.loader import render_to_string

@receiver(post_delete,sender=User)
@receiver(post_save, sender=User)
def change_user(sender, instance, *args, **kwargs):
	users = User.objects.all()
	html_users = render_to_string("includes/users.html",{'users':users})

	channel_layer = get_channel_layer()
	async_to_sync(channel_layer.group_send)(
		"users",
		{
			"type":"user_update",
			"event":"New User",
			'html_users': html_users,
		}
	)