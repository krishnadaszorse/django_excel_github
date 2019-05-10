from github import Github
from django.conf import settings

def get_authorised():
	g = Github(settings.GITHUB_TOKEN)
	return g

def get_login_user():
	g = get_authorised()
	user = g.get_user()
	return user

def get_user_by_username(username):
	try:
		g = get_authorised()
		user = g.get_user(username)
		return user
	except:
		return None

