from django.db import models


class Institution(models.Model):
    institution_abbreviation = models.CharField(max_length=30)
    institution_name = models.CharField(max_length=200)

    def __str__(self):
        return self.institution_abbreviation

    class Meta:
        ordering = ['institution_abbreviation']


class DegreeLevel(models.Model):
    degree_abbreviation = models.CharField(max_length=10)
    degree_name = models.CharField(max_length=100)

    def __str__(self):
        return self.degree_abbreviation

    class Meta:
        ordering = ['degree_abbreviation']


class Subject(models.Model):
    subject = models.CharField(max_length=255)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['subject']


class Location(models.Model):
    location = models.CharField(
        max_length=255,
        help_text=(
            "Locations should be in the format of <em>Country > State > "
            "County > Township</em>"
        ),
    )

    def __str__(self):
        return self.location

    class Meta:
        ordering = ['location']


class Citation(models.Model):
    withers_thesis_number = models.IntegerField(
        "Withers' Thesis Number",
        blank=True,
        help_text="Thesis Number",
    )
    author = models.CharField(
        max_length=255,
        help_text="Author's name formatted Last, First Middle",
    )
    initial_article = models.CharField(
        "Initital Article",
        max_length=20,
        blank=True,
        help_text="Initial Article (The, A)",
    )
    title = models.TextField(help_text="Title (omit initial article)")
    pagination = models.IntegerField(
        help_text=(
            "Number of pages formatted as number <em>55</em> <br />Note: the "
            "pp is added by the system later "
        ),
    )
    granting_institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE,
        help_text="Institution awarding Degree",
    )
    degree_level = models.ForeignKey(
        DegreeLevel,
        on_delete=models.CASCADE,
        help_text="Type of degree",
    )
    year = models.IntegerField(
        help_text="Year degree was awarded, formatted as <em>yyyy</em>",
    )
    local_call_no = models.CharField(
        "Local Call Number",
        max_length=200,
        blank=True,
    )
    abstract = models.TextField()
    subjects = models.ManyToManyField(Subject)
    coverage = models.ManyToManyField(Location, blank=True)
    citation_added_date = models.DateField(auto_now_add=True)
    citation_edited_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def full_title(self):
        return "%s %s" % (self.initial_article, self.title)

    def pagination_pretty(self):
        return "%spp" % self.pagination
