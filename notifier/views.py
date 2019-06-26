from django.shortcuts import render
from django.shortcuts import render
# from django.contrib.auth.models import User
from accounts.models import User
# from accounts.models import User
from django.views.generic import TemplateView
# Create your views here.
class HomeView(TemplateView):
     template_name='notifier/index.html'


def new_user(request):
	users = User.objects.all()

	return render(request, 'new_user.html',{'users':users})
