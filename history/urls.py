from django.urls import path
from . import views


urlpatterns = [
    path('', views.history_view, name="history_view"),
    path('all-history/', views.all_history, name="all_history"),
]