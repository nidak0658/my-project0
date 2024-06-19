from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
    path('profile/', views.candidate_profile, name='candidate_profile'),
    path('applications/', views.application_status, name='application_status'),
]
