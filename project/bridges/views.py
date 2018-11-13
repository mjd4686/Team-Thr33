from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import Survey
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

class ChartData(APIView):
    authentication_classes =[]
    permission_classes =[]
    def get(self,request,formate = None):
        articles = dict()
        for survey in Survey.objects.all():
            if not survey.major in articles:
                articles[survey.major] =1
            else:
                articles[survey.major] +=1
        articles = sorted(articles.items() , key =lambda x: x[1])
        articles = dict(articles)
        data ={
        "article_label": articles.keys(),
        "article_data":articles.values(),
        }

        return Response(data)

def survey_article_list(request):
    return render(request,"chart.html",{})