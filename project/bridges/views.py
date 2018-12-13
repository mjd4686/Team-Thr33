from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import People


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
#                        People Survey
#----------------------------------------------------------------------
from .models import People
from .forms import SurveyForm

class form(TemplateView):
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
            form = SurveyForm();
            return redirect('form');

        text = 'There was an error.'
        args = {'form':form, 'text':text}
        return render(request, self.template, args)


#----------------------------------------------------------------------
#                        Login View
#----------------------------------------------------------------------

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('signup')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
