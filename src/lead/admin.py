from django.contrib import admin

# Register your models here.
from .models import Join

class LeadAdmin(admin.ModelAdmin):
    list_display = ["lead_name", "timestamp"]

admin.site.register(Join)