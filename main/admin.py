from django.contrib import admin
from .models import StartupDetails, FunctionalRequirements, NonFunctionalRequirements

admin.site.register(StartupDetails)
admin.site.register(FunctionalRequirements)
admin.site.register(NonFunctionalRequirements)
