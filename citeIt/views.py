from django.shortcuts import render, get_object_or_404
from citeIt.models import Citation


def index(request):
    citations = Citation.objects.all().order_by('withers_thesis_number')
    return render(request, 'citeIt/index.html', {'citations': citations})


def citation(request, citation_id):
    c = get_object_or_404(Citation, pk=citation_id)
    return render(request, 'citeIt/detail.html', {'citation': c})


def author(request, author):
    author = author.replace("_", " ")
    citations = Citation.objects.filter(author__istartswith=author)
    return render(request, 'citeIt/index.html', {'citations': citations})


def authors(request):
    authors = Citation.objects.all().values('author').distinct()
    return render(request, 'citeIt/authors.html', {'authors': authors})


def institution(request, institution):
    citations = Citation.objects.filter(
        granting_institution__institution_abbreviation__exact=institution
    )
    return render(request, 'citeIt/index.html', {'citations': citations})


def degree(request, degree):
    citations = Citation.objects.filter(degree_level__degree_abbreviation__exact=degree)
    return render(request, 'citeIt/index.html', {'citations': citations})


def degrees(request):
    degrees = Citation.objects.all().values('degree_level__degree_abbreviation').distinct()
    return render(request, 'citeIt/degrees.html', {'degrees': degrees})


def year(request, year):
    citations = Citation.objects.filter(year__exact=year)
    return render(request, 'citeIt/index.html', {'citations': citations})


def subject(request, subject):
    subject = subject.replace("_", " ")
    citations = Citation.objects.filter(subjects__subject__startswith=subject)
    return render(request, 'citeIt/index.html', {'citations': citations})


def location(request, location):
    location = location.replace("_", " ")
    citations = Citation.objects.filter(coverage__location__startswith=location)
    return render(request, 'citeIt/index.html', {'citations': citations})


def about(request):
    return render(request, 'citeIt/about.html')
