from unittest import expectedFailure

from django.core.urlresolvers import resolve
from django.test import TestCase

from citeIt import views


class TestURLs(TestCase):
    """Test that the URLs are matched and resolved to the correct views."""

    def test_index_url(self):
        view = resolve('/withers/').func
        self.assertEqual(view, views.index)

    def test_about_url(self):
        view = resolve('/withers/about/').func
        self.assertEqual(view, views.about)

    def test_citation_url(self):
        view = resolve('/withers/citation/001/').func
        self.assertEqual(view, views.citation)

    def test_author_url(self):
        view = resolve('/withers/author/Logan,_John_H./').func
        self.assertEqual(view, views.author)

    # Currently the URL regex doesn't allow dashes, apostrophes, etc.
    @expectedFailure
    def test_author_url_with_special_chars(self):
        view = resolve('/withers/author/Logan-Durant,_John_H./').func
        self.assertEqual(view, views.author)

    def test_authors_url(self):
        view = resolve('/withers/author/').func
        self.assertEqual(view, views.authors)

    def test_institution_url(self):
        view = resolve('/withers/institution/UNT/').func
        self.assertEqual(view, views.institution)

    # Currently the URL regex doesn't allow ampersands.
    @expectedFailure
    def test_institution_url_with_special_chars(self):
        view = resolve('/withers/institution/A&M/').func
        self.assertEqual(view, views.institution)

    def test_degree_url(self):
        view = resolve('/withers/degree/MA/').func
        self.assertEqual(view, views.degree)

    def test_degrees_url(self):
        view = resolve('/withers/degree/').func
        self.assertEqual(view, views.degrees)

    def test_year_url(self):
        view = resolve('/withers/year/1932/').func
        self.assertEqual(view, views.year)

    def test_subject_url(self):
        view = resolve('/withers/subject/local_politics/').func
        self.assertEqual(view, views.subject)

    # Currently the URL regex doesn't allow dashes, apostrophes, etc.
    @expectedFailure
    def test_subject_url_with_special_chars(self):
        view = resolve('/withers/subject/K-12_Education/').func
        self.assertEqual(view, views.subject)

    def test_location_url(self):
        view = resolve('/withers/location/United_States/').func
        self.assertEqual(view, views.location)

    # Currently the URL regex doesn't allow the greater-than sign.
    @expectedFailure
    def test_location_url_with_special_chars(self):
        view = resolve('/withers/location/United_States_>_Texas/').func
        self.assertEqual(view, views.location)
