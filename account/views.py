from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
#from django.template import RequestContext, loader

from account.models import UserProfile
from shelf.models import *


# Create your views here.
#@login_required
def profile(request, username):
	user = UserProfile.objects.filter(user__username = username)

	try:
		character_list = user[0].character_set.all()
	except:
		raise Http404

	books = []

	for character in character_list:
		char = user[0].character_set.get(name = character)
		books.append(Book.objects.filter(character = char)[0].title)
	
	list_count = "this is a char list of count "+str(character_list.count())
	
	#template = loader.get_template('account/userprofile.html')

	context = {
		'character_list': character_list,
		'book_list': list(set(books)),
		'username': username,
		'list_count': list_count,
	}

	#return HttpResponse(template.render(context))
	#return HttpResponse("Hello, world. You're at the User Profile of "+username)
	return render(request, 'account/userprofile.html', context)