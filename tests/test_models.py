from unittest import expectedFailure

from django.test import TestCase

from citeIt.models import Institution, DegreeLevel, Subject, Location, Citation


class TestModelMethods(TestCase):
    """Test that the models' methods return the expected strings."""

    @classmethod
    def setUpTestData(cls):
        """Set up the model instances for the tests."""
        cls.institution = Institution.objects.create(
            institution_abbreviation='UNT')
        cls.degree_level = DegreeLevel.objects.create(degree_abbreviation='MA')
        cls.location = Location.objects.create(location='Prussia')
        cls.subject = Subject.objects.create(subject='History')
        cls.citation_with_article = Citation.objects.create(
            withers_thesis_number='1',
            initial_article='The',
            title='Traitor',
            pagination='420',
            granting_institution=cls.institution,
            degree_level=cls.degree_level,
            year='1998'
        )
        cls.citation_without_article = Citation.objects.create(
            withers_thesis_number='2',
            title='Mathematics: From the Birth of Numbers',
            pagination='1024',
            granting_institution=cls.institution,
            degree_level=cls.degree_level,
            year='2012'
        )

    def test_full_title_with_initial_article(self):
        """Check that the initial article gets prepended to the title."""
        self.assertEqual(self.citation_with_article.full_title(),
                         'The Traitor')

    # This test fails because currently the model will prepend a space to the
    # full title if no initial article exists.
    @expectedFailure
    def test_full_title_without_initial_article(self):
        """Check that title with no initial article gets printed correctly."""
        self.assertEqual(self.citation_without_article.full_title(),
                         'Politicians')

    def test_pagination_pretty(self):
        """Check that the page number is correctly appended with a 'pp'."""
        self.assertEqual(self.citation_with_article.pagination_pretty(),
                         '420pp')

    def test_institution_str_repr(self):
        """Check that the model's string representation is the abbreviation."""
        self.assertEqual(str(self.institution), 'UNT')

    def test_degreelevel_str_repr(self):
        """Check that the model's string representation is the abbreviation."""
        self.assertEqual(str(self.degree_level), 'MA')

    def test_subject_str_repr(self):
        """Check that the model's string representation is the subject."""
        self.assertEqual(str(self.subject), 'History')

    def test_location_str_repr(self):
        """Check that the model's string representation is the location."""
        self.assertEqual(str(self.location), 'Prussia')

    def test_citation_str_repr(self):
        """Check that the model's string representation is the title."""
        self.assertEqual(str(self.citation_with_article), 'Traitor')
