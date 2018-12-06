from django.urls import path
from bridges import views
from bridges.views import survey_article_list,ChartData
from django.contrib import admin

admin.site.site_header = "Student Bridges Admin Portal"
admin.site.site_title = "Student Bridge Admin Portal"
admin.site.index_title = "Welcome to Student Bridges Portal"
urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form.as_view(), name='form'),
    path('surveys/',views.survey_article_list,name ='surveys'),
    path('signup/', views.signup, name='signup'),
    path('api/chart/data',views.ChartData().as_view()),
    path('graph/', views.IndexView.as_view(), name='graph'),
]
