from django.contrib import admin

from blog.models import *

# Register your models here.
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class BlogTagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'to_publish', 'category', 'create_dt', 'pk', 'summary',)
    search_fields = ('title', 'summary',)
    list_filter = ['to_publish']
    filter_horizontal = ('tags',)

class BlogAttachmentAdmin(admin.ModelAdmin):
    list_display = ('blog__title', 'attachment')
    search_fields = ('blog__title',)
    list_filter = ['blog__title']

class BlogItemAdmin(admin.ModelAdmin):
    list_display = ('blog', 'is_custom', 'order', 'tag_name', 'attr_value',)
    search_fields = ('blog__title',)
    list_filter = ['blog']

admin.site.register(BlogCategory, BlogTagAdmin)
admin.site.register(BlogTag, BlogTagAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogAttachment, BlogAttachmentAdmin)
admin.site.register(BlogItem, BlogItemAdmin)
