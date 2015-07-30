from unittest import expectedFailure

from django.test import TestCase

from . import factories


class TestModelMethods(TestCase):
    """Test that the models' methods return the expected strings."""

    def test_full_title_with_initial_article(self):
        """Check that the initial article gets prepended to the title."""
        citation_with_article = factories.CitationFactory(
            initial_article='The',
            title='Traitor'
        )
        self.assertEqual(citation_with_article.full_title(), 'The Traitor')

    # This test fails because currently the model will prepend a space to the
    # full title if no initial article exists.
    @expectedFailure
    def test_full_title_without_initial_article(self):
        """Check that title with no initial article gets printed correctly."""
        factories.CitationFactory(initial_article='', title='Politicians')
        self.assertEqual(self.without_article.full_title(), 'Politicians')

    def test_pagination_pretty(self):
        """Check that the page number is correctly appended with a 'pp'."""
        citation = factories.CitationFactory(pagination='42')
        self.assertEqual(citation.pagination_pretty(), '42pp')

    def test_institution_str_repr(self):
        """Check that the model's string representation is the abbreviation."""
        institution = factories.InstitutionFactory(
            institution_abbreviation='UNT')
        self.assertEqual(str(institution), 'UNT')

    def test_degreelevel_str_repr(self):
        """Check that the model's string representation is the abbreviation."""
        degree_level = factories.DegreeLevelFactory(degree_abbreviation='MBA')
        self.assertEqual(str(degree_level), 'MBA')

    def test_subject_str_repr(self):
        """Check that the model's string representation is the subject."""
        subject = factories.SubjectFactory(subject='Alchemy')
        self.assertEqual(str(subject), 'Alchemy')

    def test_location_str_repr(self):
        """Check that the model's string representation is the location."""
        location = factories.LocationFactory(location='Russia')
        self.assertEqual(str(location), 'Russia')

    def test_citation_str_repr(self):
        """Check that the model's string representation is the title."""
        citation = factories.CitationFactory(initial_article='The',
                                             title='Wandering Mouse')
        self.assertEqual(str(citation), 'Wandering Mouse')
