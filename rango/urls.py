from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'rango.views.index', name='rango_index'),
    url(r'^about/$', 'rango.views.about', name="rango_about"),
)
