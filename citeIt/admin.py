from django.contrib import admin

from citeIt.models import Institution, DegreeLevel, Subject, Location, Citation

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    """ Institution class that determines how comment appears in admin """
    list_display = ('institution_abbreviation', 'institution_name')

@admin.register(DegreeLevel)
class DegreeLevelAdmin(admin.ModelAdmin):
    """ DegreeLevel class that determines how comment appears in admin """
    list_display = ('degree_abbreviation', 'degree_name')

@admin.register(Citation)
class CitationAdmin(admin.ModelAdmin):
    """ Citation class that determines how comment appears in admin """
    list_display = ('withers_thesis_number', 'full_title', 'author',
                    'granting_institution', 'degree_level', 'year',
                    'pagination', 'local_call_no')
    list_filter = ('granting_institution', 'year', 'degree_level')
    search_fields = ('title', 'author', 'abstract')
    ordering = ('withers_thesis_number', 'title')

admin.site.register(Subject)
admin.site.register(Location)
