"""
Factories for Institution, DegreeLevel, Location, Subject, and Citation models.
"""
from datetime import datetime

import factory

from citeIt import models


class InstitutionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Institution

    institution_abbreviation = 'UNT'
    institution_name = 'University of North Texas'


class DegreeLevelFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.DegreeLevel

    degree_abbreviation = 'MBA'
    degree_name = 'Master of Business Administration'


class LocationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Location

    location = 'United States > Texas'


class SubjectFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Subject

    subject = 'Texas'


class CitationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Citation

    withers_thesis_number = factory.Sequence(lambda n: '%d' % n)
    author = 'Verne, Jules'
    initial_article = 'The'
    title = 'Island of Doctor Moreau'
    pagination = '432'
    granting_institution = factory.SubFactory(InstitutionFactory)
    degree_level = factory.SubFactory(DegreeLevelFactory)
    year = '1984'
    local_call_no = '9401234567'
    abstract = 'A book about something'
    coverage = factory.RelatedFactory(LocationFactory)
    citation_added_date = datetime.now()
    citation_edited_date = datetime.now()

    @factory.post_generation
    def subjects(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for subject in extracted:
                self.subjects.add(subject)

    @factory.post_generation
    def coverage_locs(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for location in extracted:
                self.coverage.add(location)
