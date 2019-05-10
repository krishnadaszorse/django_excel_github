from django.shortcuts import render_to_response
from .github_app import get_user_by_username

def github_user(request):
	sucess=True
	sucess_message=''
	if request.GET.has_key('username'):
		username=request.GET.get('username')
		user = get_user_by_username(username)
		if user:
			variables = {
			'user':user,
			}
			return render_to_response('user_profile.html', variables)
		else:
			sucess=False
			sucess_message=' Username does not exist'
	variables = {
	'sucess':sucess,
	'sucess_message':sucess_message,
	}
	return render_to_response('search_users.html', variables)