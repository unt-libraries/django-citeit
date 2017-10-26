from django.conf.urls import patterns

urlpatterns = patterns(
    '',
    # Example:
    (r'^$', 'citeIt.views.index'),
    (r'^about/$', 'citeIt.views.about'),
    (r'^citation/(?P<citation_id>\d+)/$', 'citeIt.views.citation'),
    (r'^author/(?P<author>[^/]+)/$', 'citeIt.views.author'),
    (r'^author/$', 'citeIt.views.authors'),
    (r'^institution/(?P<institution>[^/]+)/$', 'citeIt.views.institution'),
    (r'^degree/(?P<degree>[^/]+)/$', 'citeIt.views.degree'),
    (r'^degree/$', 'citeIt.views.degrees'),
    (r'^year/(?P<year>\d+)/$', 'citeIt.views.year'),
    (r'^subject/(?P<subject>[^/]+)/$', 'citeIt.views.subject'),
    (r'^location/(?P<location>[^/]+)/$', 'citeIt.views.location'),
)
