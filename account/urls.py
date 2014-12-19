from django.conf.urls import patterns, url

from account import views

urlpatterns = patterns('',
    url(r'^(?P<username>\w+)/$', views.profile, name='profile'),
)