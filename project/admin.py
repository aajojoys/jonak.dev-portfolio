from django.contrib import admin
from project.models import *

# Register your models here.
class FrameworkCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class FrameworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'icon',)
    search_fields = ('name',)
    list_filter = ['category']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'description',)
    search_fields = ('title',)

class ProjectAttachmentAdmin(admin.ModelAdmin):
    list_display = ('project__title', 'attachment',)
    search_fields = ('project__title',)
    list_filter = ['project__title']

class StackAdmin(admin.ModelAdmin):
    list_display = ('project__title',)
    search_fields = ('project__title',)
    list_filter = ['project__title']

admin.site.register(FrameworkCategory, FrameworkCategoryAdmin)
admin.site.register(Framework, FrameworkAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectAttachment, ProjectAttachmentAdmin)
admin.site.register(Stack, StackAdmin)
