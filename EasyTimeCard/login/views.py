from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
import django_saml2_auth.views

# Create your views here.
def index(request):
    template_name = 'login/index.html'
    return render(request,template_name)

@login_required
def dashboard(request):
    user = request.user
    auth0user = user.social_auth.get(provider="auth0")
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture']
    }

    return render(request, 'login/dashboard.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4)
    })
