from django.urls import path
from citeIt import views

app_name = 'citeIt'
urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('citation/<int:citation_id>/', views.citation),
    path('author/<str:author>/', views.author),
    path('author/', views.authors),
    path('institution/<str:institution>/', views.institution),
    path('degree/<str:degree>/', views.degree),
    path('degree/', views.degrees),
    path('year/<int:year>/', views.year),
    path('subject/<str:subject>/', views.subject),
    path('location/<str:location>/', views.location),
]
