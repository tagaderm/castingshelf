from django.db import models
from datetime import time



# Create your models here.
class Character(models.Model):
	actors = models.ManyToManyField('Actor', null=True, blank=True, related_query_name='character', db_table='character_actor_relation')
	books = models.ManyToManyField('Book', null=True, blank=True, related_query_name='character', db_table='character_book_relation')
	name = models.CharField(max_length=50)
	votes = models.IntegerField('Votes', null=True, blank=True)
	userprofile = models.ForeignKey('account.UserProfile', null=True, blank=True, related_query_name='character')
	
	
	def __str__(self):              # __unicode__ on Python 
		return self.name

class Actor(models.Model):
	url = models.URLField(null=True, blank=True)
	picture = models.ImageField(upload_to='mysite/static/char_images',blank=True)
	name = models.CharField(max_length=50,unique=True)

	def __str__(self):              # __unicode__ on Python 
		return self.name

class Comment(models.Model):
	character = models.ForeignKey('Character', null=True, blank=True)
	parent = models.ForeignKey('self', null=True, blank=True)
	user = models.CharField("User",max_length=50)
	created_on = models.DateTimeField("Comment Updated",auto_now = True)
	text = models.CharField("Comment Text",max_length=2000,blank=True)

	def __str__(self):              # __unicode__ on Python 
		return self.user+" "+str(self.created_on)[:19]

class Book(models.Model):
	#characters = models.ForeignKey('Character', null=True, blank=True)
	title = models.CharField('Title', max_length=100, null=True, unique=True)
	author = models.CharField('Author', max_length=50, null=True)
	series = models.CharField('Series', max_length=100, null=True, blank=True)
	picture = models.ImageField(upload_to='mysite/static/book_images', null=True, blank=True)

	def __str__(self):              # __unicode__ on Python 
		return self.title