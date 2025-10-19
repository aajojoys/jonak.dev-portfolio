from django.urls import path

from project.views import *

urlpatterns = [
    path("", project_view, name="project"),
    path("<uuid:project_id>/", project_detail_view, name="project_detail"),
]
