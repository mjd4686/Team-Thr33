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

from .models import Survey
from .forms import SurveyForm
class surveyform(TemplateView):
    """
    View function for form.html
    """
    # Render the HTML template index.html with the data in the context variable
    template = 'form.html'

    def get(self, request):
        form = SurveyForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = SurveyForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user= request.user
            data.save()
            form = SurveyForm()
            return redirect('form')

        text = 'There was an error.'
        args = {'form':form, 'text':text}
        return render(request, self.template, args)


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
            user.profile.year = form.cleaned_data.get('year')
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.school = form.cleaned_data.get('school')
            user.profile.major = form.cleaned_data.get('major')
            user.profile.poc = form.cleaned_data.get('poc')
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.firstgen = form.cleaned_data.get('firstgen')
            user.profile.trans = form.cleaned_data.get('trans')
            user.profile.pronoun = form.cleaned_data.get('pronoun')
            user.profile.info = form.cleaned_data.get('info')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
