
from django.urls import path
from bridges import views
from django.contrib import admin
from django.conf.urls import include

admin.site.site_header = "Student Bridges Admin Portal"
admin.site.site_title = "Student Bridge Admin Portal"
admin.site.index_title = "Welcome to Student Bridges Portal"
urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form.as_view(), name='form'),
    path('surveys/',views.survey_article_list,name ='surveys'),
    path('survey/', include('survey.urls'))
]
