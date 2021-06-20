from django.urls import path, include
from PR import views



urlpatterns = [
    path('application', views.application, name = 'application'),
    path('applicant_info_method', views.applicant_info_method, name = 'applicant_info_method'),
]

