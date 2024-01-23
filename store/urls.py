from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.main_store, name='main_store'),
    path('item/<slug:slug>/', views.offer_detail, name="offer_detail"),

]