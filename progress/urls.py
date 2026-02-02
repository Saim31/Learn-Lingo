from django.urls import path
from . import views

urlpatterns = [
    # Example: Progress dashboard (you can add more later)
    path('', views.dashboard, name='progress_dashboard'),
]
