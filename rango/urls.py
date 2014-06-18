from django.conf.urls import patterns, include, url

urlpatterns = patterns('rango.views',
    url(r'^$', 'index', name='index'),
    url(r'^about/$', 'about', name="about"),
    url(r'^category/(?P<category_name_url>\w+)/$', 'category', name="category"),
    url(r'^add_category/$', 'add_category', name="add_category"),
    url(r'^add_page/(?P<category_name_url>\w+)/$', 'add_page', name="add_page"),
)
