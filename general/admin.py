from django.contrib import admin
from general.models import *

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'value',)
    search_fields = ('name',)

class StatementAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Link, LinkAdmin)
admin.site.register(Statement, StatementAdmin)
