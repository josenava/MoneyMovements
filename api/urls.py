from django.conf.urls import url, include
from api import views
from rest_framework.authtoken import views as auth_views


urlpatterns = [
    url(r'^token-auth/', auth_views.obtain_auth_token),
    url('^auth/', include('rest_framework.urls')),
    url(r'^categories/$', views.CategoryList.as_view()),
    url(r'^categories/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
    url(r'^movements/$', views.MovementList.as_view()),
    url(r'^movements/(?P<pk>[0-9]+)/$', views.MovementDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^bulk-upload/', views.BulkUpload.as_view()),
]