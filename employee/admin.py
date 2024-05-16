from django.contrib import admin
from .models import Area, DocumentType, Person, PhotoPerson, Vote, Description

# Register your models here.
admin.site.register(Area)
admin.site.register(DocumentType)
# admin.site.register(Person)
admin.site.register(PhotoPerson)
# admin.site.register(Vote)
# admin.site.register(Description)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'identification', 'display_area', 'state')
    list_filter = ('state', 'id_area')

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('period', 'display_area', 'vote_date')
    list_filter = ('period', 'id_area', 'vote_date')


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('id_voter', 'id_voted', 'id_vote')