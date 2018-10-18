from django.shortcuts import render, redirect
from django.views.generic import TemplateView

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
#from django.http import HttpResponseRedirect
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
