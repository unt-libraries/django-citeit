from unittest import expectedFailure

from django.test import TestCase

from . import factories


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
        first_citation = factories.CitationFactory()
        factories.CitationFactory()

        response = self.client.get('/withers/citation/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['citation'], first_citation)

    def test_query_no_matching_citation(self):
        response = self.client.get('/withers/citation/2/')
        self.assertEqual(response.status_code, 404)


class TestAuthorView(TestCase):
    """Test that the author view functions correctly."""

    def test_correct_template_used(self):
        response = self.client.get('/withers/author/Some_Body/')
        self.assertTemplateUsed(response, 'citeIt/index.html')

    def test_query_matching_authors(self):
        # Create ten citations to match the query and one that doesn't.
        factories.CitationFactory.create_batch(5, author='Verne, Jules')
        factories.CitationFactory.create_batch(5, author='Verne, Jules Gabriel')
        factories.CitationFactory(author='Dan Longshot')

        response = self.client.get('/withers/author/Verne,_Jules/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['citations']), 10)

    def test_query_no_matching_author(self):
        response = self.client.get('/withers/author/No_Body/')
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
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['citations']) == 10)

    def test_query_no_matching_institutions(self):
        response = self.client.get('/withers/institution/UML/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['citations']), 0)


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
        self.assertEqual(response.status_code, 200)
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
        self.assertEqual(response.status_code, 200)
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

    # Currently a citation with multiple subjects that match will be listed
    # multiple times. Need to add distinct() to query.
    @expectedFailure
    def test_query_matching_subjects(self):
        # Create three subjects, two of which have a common prefix.
        subject_texas_history = factories.SubjectFactory(
            subject='Texas History')
        subject_texas_historians = factories.SubjectFactory(
            subject='Texas Historians')
        subject_flowers = factories.SubjectFactory(subject='Flowers')

        # Create ten citations with both similar subject, and one with the
        # unique subject.
        factories.CitationFactory.create_batch(
            10,
            subjects=(subject_texas_history, subject_texas_historians)
        )
        factories.CitationFactory(subjects=(subject_flowers, ))

        response = self.client.get('/withers/subject/Texas_Histor/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['citations']), 10)

    def test_query_no_matching_subjects(self):
        response = self.client.get('/withers/subject/flooping/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['citations']), 0)


class TestLocationView(TestCase):
    """Test that the location view functions correctly."""

    def test_correct_template_used(self):
        response = self.client.get('/withers/location/United_States/')
        self.assertTemplateUsed(response, 'citeIt/index.html')

    # Currently a citation with multiple locations that match will be listed
    # multiple times. Need to add distinct() to query.
    @expectedFailure
    def test_query_matching_locations(self):
        # Create three locations, two of which have a common prefix.
        location_south_africa = factories.LocationFactory(
            location='South Africa')
        location_south_korea = factories.LocationFactory(
            location='South Korea')
        location_mexico = factories.LocationFactory(location='Mexico')

        # Create ten citations with the two similar locations, and one with
        # the unique location.
        factories.CitationFactory.create_batch(
            10,
            coverage=(location_south_africa, location_south_korea)
        )
        factories.CitationFactory(coverage=(location_mexico, ))

        response = self.client.get('/withers/location/South_/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['citations']), 10)

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
