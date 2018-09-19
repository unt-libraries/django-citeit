from django.conf.urls import url
from citeIt import views

app_name = 'citeIt'
urlpatterns = [
    url(r'^$', views.index),
    url(r'^about/$', views.about),
    url(r'^citation/(?P<citation_id>\d+)/$', views.citation),
    url(r'^author/(?P<author>[^/]+)/$', views.author),
    url(r'^author/$', views.authors),
    url(r'^institution/(?P<institution>[^/]+)/$', views.institution),
    url(r'^degree/(?P<degree>[^/]+)/$', views.degree),
    url(r'^degree/$', views.degrees),
    url(r'^year/(?P<year>\d+)/$', views.year),
    url(r'^subject/(?P<subject>[^/]+)/$', views.subject),
    url(r'^location/(?P<location>[^/]+)/$', views.location),
]
