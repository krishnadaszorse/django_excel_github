from django.conf.urls import patterns, url
from .views import github_user

urlpatterns = patterns('',
	url(r'^github-user/$',github_user, name='github_user'),
)