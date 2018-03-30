from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^categories/$', views.CategoryList.as_view()),
    # url(r'^categories/(?P<pk>[0-9]+)/$', views.category_detail),
]