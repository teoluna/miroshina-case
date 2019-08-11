from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Rating, Profile

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    # list_display = ('name', 'slug', 'description', 'pe_ratio',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Rating)