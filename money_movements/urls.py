from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^api/', include('apiApp.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('baseApp.urls')),
    url(r'^', include('userApp.urls')),
]
