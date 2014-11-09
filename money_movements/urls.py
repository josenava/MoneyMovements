from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'money_movements.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'baseApp.views.index'),
    url(r'^api/', include('apiApp.urls')),
    url(r'^login/', 'userApp.views.user_login'),
    url(r'^sign_up/', 'userApp.views.sign_up'),
    url(r'^admin/', include(admin.site.urls)),
)
