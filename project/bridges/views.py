from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Profile


# Create your views here.

def index(request):
    """
    View function for home page of site.
    """
        # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
    )


#----------------------------------------------------------------------
#                        Login View
#----------------------------------------------------------------------

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
