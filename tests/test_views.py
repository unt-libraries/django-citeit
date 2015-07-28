import factory
from django.test import TestCase, RequestFactory

from . import factories
from citeIt import views
from citeIt.models import Institution, DegreeLevel, Citation


class TestIndexView(TestCase):
    """Test that the index view functions correctly."""

    def test_correct_template_used(self):
        response = self.client.get('/withers/')
        self.assertTemplateUsed(response, 'citeIt/index.html')

    def test_index_loads(self):
        factories.CitationFactory.create_batch(30)
        response = self.client.get('/withers/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['citations']), 30)

class TestCitationView(TestCase):
    """Test that the citation view functions correctly."""

    def test_correct_template_used(self):
        factories.CitationFactory(withers_thesis_number='1')
        response = self.client.get('/withers/citation/1/')
        self.assertTemplateUsed(response, 'citeIt/detail.html')

    def test_query_matching_citation(self):
        # Create one citation that matches the query and one that doesn't.
        first = factories.CitationFactory()
        second = factories.CitationFactory()
        response = self.client.get('/withers/citation/1/')
        self.assertTrue(response.context['citation'] == first)
        self.assertEqual(response.context['citation'], first)

    def test_query_no_matching_citation(self):
        response = self.client.get('/withers/citation/2/')
        self.assertEqual(response.status_code, 404)


class TestAuthorView(TestCase):
    """Test that the author view functions correctly."""

    def test_correct_template_used(self):
        response = self.client.get('/withers/author/Some Body/')
        self.assertTemplateUsed(response, 'citeIt/index.html')

    def test_query_matching_authors(self):
        # Create ten citations to match the query and one that doesn't.
        factories.CitationFactory.create_batch(10, author='Verne, Jules')
        factories.CitationFactory(author='Dan Longshot')
        response = self.client.get('/withers/author/Verne, Jules/')
        self.assertEqual(len(response.context['citations']), 10)

    def test_query_no_matching_author(self):
        response = self.client.get('/withers/author/No Body/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['citations']), 0)


class TestAuthorsView(TestCase):
    """Test that the authors view functions correctly."""

    def test_correct_template_used(self):
        response = self.client.get('/withers/author/')
        self.assertTemplateUsed(response, 'citeIt/authors.html')

    def test_authors_list_loads(self):
        factories.CitationFactory()
        response = self.client.get('/withers/author/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['authors']), 1)


class TestInstitutionView(TestCase):
    """Test that the institution view functions correctly."""

    def test_correct_template_used(self):
        response = self.client.get('/withers/institution/UNT/')
        self.assertTemplateUsed(response, 'citeIt/index.html')

    def test_query_matching_institutions(self):
        # Create ten citations to match the query and one that doesn't.
        factories.CitationFactory.create_batch(10)
        factories.CitationFactory(
            granting_institution=factories.InstitutionFactory(
                institution_abbreviation='M&M'
            )
        )

        response = self.client.get('/withers/institution/UNT/')
        self.assertTrue(len(response.context['citations']) == 10)

    def test_query_no_matching_institutions(self):
        response = self.client.get('/withers/institution/UML/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['citations']),  0)


class TestDegreeView(TestCase):
    """Test that the degree view functions correctly."""

    def test_correct_template_used(self):
        response = self.client.get('/withers/degree/MBA/')
        self.assertTemplateUsed(response, 'citeIt/index.html')

    def test_query_matching_degrees(self):
        # Create ten citations to match the query and one that doesn't.
        factories.CitationFactory.create_batch(10)
        factories.CitationFactory(
            degree_level=factories.DegreeLevelFactory(
                degree_abbreviation='UNO'
            )
        )

        response = self.client.get('/withers/degree/MBA/')
        self.assertEqual(len(response.context['citations']), 10)

    def test_query_no_matching_degrees(self):
        response = self.client.get('/withers/degree/PHD/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['citations']), 0)


class TestDegreesView(TestCase):
    """Test that the degrees view functions correctly."""

    def test_correct_template_used(self):
        response = self.client.get('/withers/degree/')
        self.assertTemplateUsed(response, 'citeIt/degrees.html')

    def test_degrees_list_loads(self):
        factories.CitationFactory()
        response = self.client.get('/withers/degree/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['degrees']), 1)


class TestYearView(TestCase):
    """Test that the year view functions correctly."""

    def test_correct_template_used(self):
        response = self.client.get('/withers/year/1932/')
        self.assertTemplateUsed(response, 'citeIt/index.html')

    def test_query_matching_years(self):
        # Create ten citations to match the query and one that doesn't.
        factories.CitationFactory.create_batch(10)
        factories.CitationFactory(year='2015')
        response = self.client.get('/withers/year/1984/')
        self.assertEqual(len(response.context['citations']), 10)

    def test_query_no_matching_year(self):
        response = self.client.get('/withers/year/0000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['citations']), 0)


class TestSubjectView(TestCase):
    """Test that the subject view functions correctly."""

    def test_correct_template_used(self):
        response = self.client.get('/withers/subject/weather/')
        self.assertTemplateUsed(response, 'citeIt/index.html')

   #def test_query_matching_subjects(self):
   #    # Create ten citations to match the query and one that doesn't.
   #    factories.CitationFactory.create_batch(10)
   #    response = self.client.get('/withers/subject/Texas/')
   #    self.assertEqual(len(response.context['citations']), 10)

    def test_query_no_matching_subjects(self):
        response = self.client.get('/withers/subject/flooping/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['citations']), 0)


class TestLocationView(TestCase):
    """Test that the location view functions correctly."""

    def test_correct_template_used(self):
        response = self.client.get('/withers/location/United_States/')
        self.assertTemplateUsed(response, 'citeIt/index.html')

#   def test_query_matching_locations(self):
#       # Create ten citations to match the query and one that doesn't.
#       hold = factories.CitationFactory.create_batch(10)
#       response = self.client.get('/withers/location/United_States/')
#       self.assertEqual(len(response.context['citations']), 10)

    def test_query_no_matching_locations(self):
        response = self.client.get('/withers/location/Untied_Spades/')
        self.assertEqual(response.status_code, 200)


class TestAboutView(TestCase):
    """Test that the about view functions correctly."""

    def test_correct_template_used(self):
        response = self.client.get('/withers/about/')
        self.assertTemplateUsed(response, 'citeIt/about.html')

    def test_about_loads(self):
        response = self.client.get('/withers/about/')
        self.assertEqual(response.status_code, 200)
