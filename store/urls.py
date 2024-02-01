from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
import store.views

app_name = 'store'

urlpatterns = [
    path('', views.main_store, name='main_store'),
    path('item/<slug:slug>/', views.offer_detail, name="offer_detail"),
    path('search/<slug:category_slug>/', views.category_list_view, name="category_list_view"),
    path('ajax-add-review/<id>', views.ajax_add_review, name="ajax-add-review"),
    path('load-more-data', views.load_more_data, name="load-more-data"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)