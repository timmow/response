from django.contrib import admin
from core.models import Incident, Action, ExternalUser, IncidentExtension

admin.site.register(Action)
admin.site.register(Incident)
admin.site.register(ExternalUser)
admin.site.register(IncidentExtension)
