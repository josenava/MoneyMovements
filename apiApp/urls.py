from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^import/', views.import_file),
    url(r'^add/', views.add_movement),
    url(r'^movements/(?P<nMov>\d+)/$', views.get_movements),
    url(r'^categories/$', views.categories_api_calls),
    url(r'^categories/(?P<name>\w+)/$', views.categories_api_calls),
]
