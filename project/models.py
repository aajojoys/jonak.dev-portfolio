import uuid

from django.db import models
from utility.model_utils import imagefield_rename_upload, imagefield_upload

MEDIA_PROJECT_ATTACHMENT_RELATIVEPATH = "project/attachment"
MEDIA_PROJECT_FRAMEWORK_RELATIVEPATH = "project/framework"

# Create your models here.
def upload_project_image(instance, filename):
    return imagefield_rename_upload(instance, filename, MEDIA_PROJECT_ATTACHMENT_RELATIVEPATH)

def upload_framework_icon(instance, filename):
    return imagefield_upload(instance, filename, MEDIA_PROJECT_FRAMEWORK_RELATIVEPATH)

class FrameworkCategory(models.Model):
    name = models.CharField(
        max_length=32,
        unique=True,
    )

    def __str__(self):
        return f"{self.pk} - {self.name}"

class Framework(models.Model):
    # framework or programming languages
    name = models.CharField(
        max_length=32,
        unique=True,
    )
    category = models.ForeignKey(
        'project.FrameworkCategory',
        on_delete=models.CASCADE
    )
    icon = models.ImageField(
        null=True,
        blank=True,
        upload_to=upload_framework_icon,
    )

    def __str__(self):
        return f"{self.pk} - {self.name} ({self.category})"

class ProjectTag(models.Model):
    name = models.CharField(
        max_length=32,
        unique=True,
    )

    def __str__(self):
        return f"{self.pk} - {self.name}"

class Project(models.Model):
    # project info
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(
        max_length=32,
        unique=True,
    )
    # short description of project
    summary = models.TextField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    tag = models.ForeignKey(
        'project.ProjectTag',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.title} ({self.pk})"

class ProjectAttachment(models.Model):
    # project image attachment
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
    )
    attachment = models.ImageField(
        upload_to=upload_project_image,
    )

class Stack(models.Model):
    # techstack of project (one of more frameworks)
    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
    )
    frameworks = models.ManyToManyField(
        'project.Framework',
    )
