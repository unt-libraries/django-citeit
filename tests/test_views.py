from django.test import TestCase, RequestFactory

from citeIt import views
from citeIt.models import Institution, DegreeLevel, Citation


class TestIndexView(TestCase):
    """Test that the index view functions correctly."""

    def test_returns_200_on_valid_request(self):
        """Set up a couple database entries to use in the tests."""
        status_code = self.client.get('/withers/').status_code
        self.assertEqual(status_code, 200)


class TestCitationView(TestCase):
    """Test that the citation view functions correctly."""

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


    def test_returns_200_on_valid_request(self):
        status_code = self.client.get('/withers/citation/001/').status_code
        self.assertEqual(status_code, 200)


class TestAuthorView(TestCase):
    """Test that the author view functions correctly."""

    def test_returns_200_on_valid_request(self):
        status_code = self.client.get('/withers/author/Some Body/').status_code
        self.assertEqual(status_code, 200)


class TestAuthorsView(TestCase):
    """Test that the authors view functions correctly."""

    def test_returns_200_on_valid_request(self):
        status_code = self.client.get('/withers/author/').status_code
        self.assertEqual(status_code, 200)


class TestInstitutionView(TestCase):
    """Test that the institution view functions correctly."""

    def test_returns_200_on_valid_request(self):
        status_code = self.client.get('/withers/institution/UNT/').status_code
        self.assertEqual(status_code, 200)


class TestDegreeView(TestCase):
    """Test that the degree view functions correctly."""

    def test_returns_200_on_valid_request(self):
        status_code = self.client.get('/withers/degree/MBA/').status_code
        self.assertEqual(status_code, 200)


class TestDegreesView(TestCase):
    """Test that the degrees view functions correctly."""

    def test_returns_200_on_valid_request(self):
        status_code = self.client.get('/withers/degree/').status_code
        self.assertEqual(status_code, 200)


class TestYearView(TestCase):
    """Test that the year view functions correctly."""

    def test_returns_200_on_valid_request(self):
        status_code = self.client.get('/withers/year/1932/').status_code
        self.assertEqual(status_code, 200)


class TestSubjectView(TestCase):
    """Test that the subject view functions correctly."""

    def test_returns_200_on_valid_request(self):
        status_code = self.client.get('/withers/subject/weather/').status_code
        self.assertEqual(status_code, 200)


class TestLocationView(TestCase):
    """Test that the location view functions correctly."""

    def test_returns_200_on_valid_request(self):
        status_code = self.client.get('/withers/location/United_States/').status_code
        self.assertEqual(status_code, 200)


class TestAboutView(TestCase):
    """Test that the about view functions correctly."""

    def test_returns_200_on_valid_request(self):
        status_code = self.client.get('/withers/about/').status_code
        self.assertEqual(status_code, 200)
