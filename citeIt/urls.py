from django.conf.urls import *

urlpatterns = patterns('',
    # Example:
    (r'^$', 'citeIt.views.index'),
    (r'^about/$', 'citeIt.views.about'),
    (r'^citation/(?P<citation_id>\d+)/$', 'citeIt.views.citation'),
    (r'^author/(?P<author>[\w,.\s]+)/$', 'citeIt.views.author'),
    (r'^author/$', 'citeIt.views.authors'),
    (r'^institution/(?P<institution>\w+)/$', 'citeIt.views.institution'),
    (r'^degree/(?P<degree>\w+)/$', 'citeIt.views.degree'),
    (r'^degree/$', 'citeIt.views.degrees'),
    (r'^year/(?P<year>\d+)/$', 'citeIt.views.year'),
    (r'^subject/(?P<subject>\w+)/$', 'citeIt.views.subject'),
    (r'^location/(?P<location>\w+)/$', 'citeIt.views.location'),
)
