from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='mysite/static/profile_images', null=True, blank=True)
	#name = models.CharField(User.get_username(User.self))
	
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			UserProfile.objects.create(user=instance)

		post_save.connect(create_user_profile, sender=User)

	def __unicode__(self):
		return self.user.username

