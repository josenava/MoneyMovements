from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^import/', 'apiApp.views.importFile'),
                       url(r'^add/', 'apiApp.views.addMovement'),
                       url(r'^movements/(?P<nMov>[0-9]+)/$', 'apiApp.views.getMovements'),
                       )