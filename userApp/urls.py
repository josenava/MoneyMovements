from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.user_login, name='user-login'),
    url(r'^logout$', views.user_logout, name='user-logout'),
    url(r'^sign_up$', views.sign_up, name='sign-up'),
]
