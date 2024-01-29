from django.urls import path
from . import views
import store.views

app_name = 'store'

urlpatterns = [
    path('', views.main_store, name='main_store'),
    path('item/<slug:slug>/', views.offer_detail, name="offer_detail"),
    path('search/<slug:category_slug>/', views.category_list_view, name="category_list_view"),
    path('ajax-add-review/<id>/', views.ajax_add_review, name="ajax-add-review"),
    #path('submit_review/<slug:offer>/', views.submit_review, name="submit_review"),

]