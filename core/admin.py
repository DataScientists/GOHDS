from django.contrib import admin
from core.models import Domain, Indicator

class IndicatorInline(admin.TabularInline):
    model = Indicator
    hide_name = False
    extra = 0

class DomainAdmin(admin.ModelAdmin):
    inlines = [IndicatorInline]
admin.site.register(Domain, DomainAdmin)
