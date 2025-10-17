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

class ProjectTagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'to_publish', 'tag', 'summary', 'description',)
    search_fields = ('title',)
    list_filter = ['to_publish']

class ProjectAttachmentAdmin(admin.ModelAdmin):
    list_display = ('project__title', 'title', 'attachment',)
    search_fields = ('title', 'project__title')
    list_filter = ['project__title']

class StackAdmin(admin.ModelAdmin):
    list_display = ('project__title',)
    search_fields = ('project__title',)
    list_filter = ['project__title']
    filter_horizontal = ('frameworks',)

admin.site.register(FrameworkCategory, FrameworkCategoryAdmin)
admin.site.register(Framework, FrameworkAdmin)
admin.site.register(ProjectTag, ProjectTagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectAttachment, ProjectAttachmentAdmin)
admin.site.register(Stack, StackAdmin)
