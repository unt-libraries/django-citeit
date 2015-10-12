from django.contrib import admin
#Auth Models
from django.contrib.auth.models import User, Group
#Auth Admins
from django.contrib.auth.admin import UserAdmin, GroupAdmin
#citeIt Models
from citeIt.models import DegreeLevel, Subject, Citation
from citeIt.models import Location as citeIt_Location
from citeIt.models import Institution as citeIt_Institution
#citeIt Admins
from citeIt.admin import DegreeLevelAdmin, CitationAdmin
from citeIt.admin import InstitutionAdmin as citeIt_InstitutionAdmin
#Register all the admin objects that live in the main admin
main_admin = admin.AdminSite(name="main")
#Auth
main_admin.register(User, UserAdmin)
main_admin.register(Group, GroupAdmin)
#citeIt
main_admin.register(citeIt_Institution, citeIt_InstitutionAdmin)
main_admin.register(DegreeLevel, DegreeLevelAdmin)
main_admin.register(Subject)
main_admin.register(citeIt_Location)
main_admin.register(Citation, CitationAdmin)
