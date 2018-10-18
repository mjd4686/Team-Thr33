from django.urls import path
from bridges import views


urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form.as_view(), name='form'),
]
