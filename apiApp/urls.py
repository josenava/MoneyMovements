from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^import/', 'apiApp.views.import_file'),
                       url(r'^add/', 'apiApp.views.add_movement'),
                       url(r'^movements/(?P<nMov>[0-9]+)/$', 'apiApp.views.get_movements'),
                       url(r'^categories/$', 'apiApp.views.categories_api_calls'),
                       url(r'^categories/(?P<name>\w+)/$', 'apiApp.views.categories_api_calls'),
                       )