from django.urls import path
from reports import views

urlpatterns = [
    path('', views.report_form, name='report_form'),
    path('generate/', views.generate_report, name='generate_report'),
]