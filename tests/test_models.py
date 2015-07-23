from unittest import expectedFailure

from django.test import TestCase

from citeIt.models import Institution, DegreeLevel, Citation


class TestCitationMethods(TestCase):
    """Test that the Citation model's methods return the expected strings."""

    @classmethod
    def setUpTestData(cls):
        """Set up a couple database entries to use in the tests."""
        institution = Institution.objects.create(
            institution_abbreviation='UNM',
            institution_name='University of Northern Mars'
        )

        degree = DegreeLevel.objects.create(
            degree_abbreviation='MM',
            degree_name='Master Mind'
        )

        cls.with_article = Citation.objects.create(
            withers_thesis_number=001,
            author='Martian, Martin M',
            initial_article='The',
            title='Traitor',
            pagination=42,
            granting_institution=institution,
            degree_level=degree,
            year=2020,
            local_call_no='000-000-0001',
            abstract='No abstract.'
        )

        cls.without_article = Citation.objects.create(
            withers_thesis_number=002,
            author='Martian, Martin M',
            title='Politicians',
            pagination=24,
            granting_institution=institution,
            degree_level=degree,
            year=2020,
            local_call_no='000-000-0001',
            abstract='No abstract.'
        )

    def test_full_title_with_initial_article(self):
        """Check that the initial article gets prepended to the title."""
        self.assertEqual(self.with_article.full_title(), 'The Traitor')

    # This test fails because currently the model will prepend a space to the
    # full title if no initial article exists.
    @expectedFailure
    def test_full_title_without_initial_article(self):
        """Check that title with no initial article gets printed correctly."""
        self.assertEqual(self.without_article.full_title(), 'Politicians')

    def test_pagination_pretty(self):
        """Check that the page number is correctly appended with a 'pp'."""
        self.assertEqual(self.with_article.pagination_pretty(), '42pp')
