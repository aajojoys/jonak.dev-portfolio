import uuid

from django.db import models

from utility.model_utils import imagefield_rename_upload

MEDIA_BLOG_ATTACHMENT_RELATIVEPATH = "blog/attachment"
MEDIA_BLOG_ITEM_RELATIVEPATH = "blog/item"

# Create your models here.
def upload_blog_image(instance, filename):
    return imagefield_rename_upload(instance, filename, MEDIA_BLOG_ATTACHMENT_RELATIVEPATH)

def upload_item_image(instance, filename):
    return imagefield_rename_upload(instance, filename, MEDIA_BLOG_ITEM_RELATIVEPATH)

class BlogCategory(models.Model):
    name = models.CharField(
        max_length=32,
        unique=True,
    )

    def __str__(self):
        return f"{self.name} ({self.pk})"

class BlogTag(models.Model):
    name = models.CharField(
        max_length=32,
        unique=True,
    )

    def __str__(self):
        return f"{self.name} ({self.pk})"

class Blog(models.Model):
    category = models.ForeignKey(
        'blog.BlogCategory',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    create_dt = models.DateTimeField(
        auto_now_add=False,
        auto_now=False,
    )
    title = models.CharField(
        max_length=128,
        unique=True,
    )
    summary = models.TextField(
        null=True,
        blank=True,
    )
    tags = models.ManyToManyField(
        'blog.BlogTag',
    )

    def __str__(self):
        return f"{self.title} ({self.pk})"

class BlogAttachment(models.Model):
    blog = models.ForeignKey(
        'blog.Blog',
        on_delete=models.CASCADE,
    )
    attachment = models.ImageField(
        upload_to=upload_blog_image,
    )

class BlogItem(models.Model):
    # if tag_name is null & attr_value is empty -> custom HTML content (stacked tag name)
    blog = models.ForeignKey(
        'blog.Blog',
        on_delete=models.CASCADE,
    )
    is_custom = models.BooleanField()
    # is_default takes default css style corresponding to its HTML tag
    is_default = models.BooleanField(
        default=True,
    )
    # HTML tag name
    tag_name = models.CharField(
        max_length=16,
        null=True,
        blank=True,
    )
    # HTML attr e.g. class, etc
    attr_value = models.JSONField(
        default=dict,
        blank=True,
    )
    content = models.TextField(
        null=True,
        blank=True,
    )
    attachment = models.ImageField(
        upload_to=upload_item_image,
        null=True,
        blank=True,
    )
    # order with 0 indicates first element
    order = models.PositiveSmallIntegerField()

    # blogitem tagged with same  id must have different ordering
    class Meta:
        unique_together = ["blog", "order"]
