from imp import SEARCH_ERROR
from django.contrib import admin
from .models import Project, Review, Tag


class Filtre(admin.ModelAdmin):

    search_fields = ['title']

admin.site.register(Project, Filtre)
admin.site.register(Review)
admin.site.register(Tag)

