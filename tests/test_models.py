from unittest import expectedFailure

from django.test import TestCase

from citeIt.models import Institution, DegreeLevel, Subject, Location, Citation


class TestModelMethods(TestCase):
    """Test that the models' methods return the expected strings."""

    def test_full_title_with_initial_article(self):
        """Check that the initial article gets prepended to the title."""
        institution = Institution.objects.create(
            institution_abbreviation='UNT')
        degree = DegreeLevel.objects.create(
            degree_abbreviation='MBA')
        citation_with_article = Citation.objects.create(
            withers_thesis_number='1',
            initial_article='The',
            title='Traitor',
            pagination='42',
            granting_institution=institution,
            degree_level=degree,
            year='1998',
        )
        self.assertEqual(citation_with_article.full_title(), 'The Traitor')

    # This test fails because currently the model will prepend a space to the
    # full title if no initial article exists.
    @expectedFailure
    def test_full_title_without_initial_article(self):
        """Check that title with no initial article gets printed correctly."""
        institution = Institution.objects.create(
            institution_abbreviation='UNT')
        degree = DegreeLevel.objects.create(
            degree_abbreviation='MBA')
        citation_without_article = Citation.objects.create(
            withers_thesis_number='1',
            title='Politicians',
            pagination='42',
            granting_institution=institution,
            degree_level=degree,
            year='1998',
        )
        self.assertEqual(citation_without_article.full_title(), 'Politicians')

    def test_pagination_pretty(self):
        """Check that the page number is correctly appended with a 'pp'."""
        institution = Institution.objects.create(
            institution_abbreviation='UNT')
        degree = DegreeLevel.objects.create(
            degree_abbreviation='MBA')
        citation = Citation.objects.create(
            withers_thesis_number='1',
            pagination='42',
            granting_institution=institution,
            degree_level=degree,
            year='1998',
        )
        self.assertEqual(citation.pagination_pretty(), '42pp')

    def test_institution_str_repr(self):
        """Check that the model's string representation is the abbreviation."""
        institution = Institution.objects.create(
            institution_abbreviation='UNT')
        self.assertEqual(str(institution), 'UNT')

    def test_degreelevel_str_repr(self):
        """Check that the model's string representation is the abbreviation."""
        degree_level = DegreeLevel.objects.create(degree_abbreviation='MBA')
        self.assertEqual(str(degree_level), 'MBA')

    def test_subject_str_repr(self):
        """Check that the model's string representation is the subject."""
        subject = Subject.objects.create(subject='Alchemy')
        self.assertEqual(str(subject), 'Alchemy')

    def test_location_str_repr(self):
        """Check that the model's string representation is the location."""
        location = Location.objects.create(location='Russia')
        self.assertEqual(str(location), 'Russia')

    def test_citation_str_repr(self):
        """Check that the model's string representation is the title."""
        institution = Institution.objects.create(
            institution_abbreviation='UNT')
        degree = DegreeLevel.objects.create(
            degree_abbreviation='MBA')
        citation = Citation.objects.create(
            withers_thesis_number='1',
            initial_article='The',
            title='Wandering Mouse',
            pagination='42',
            granting_institution=institution,
            degree_level=degree,
            year='1998',
        )
        self.assertEqual(str(citation), 'Wandering Mouse')
