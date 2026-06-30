from django.urls import path

from download.views import *
from download.resume_views import ResumeDownloadView

urlpatterns = [
    path("resume/", ResumeDownloadView.as_view(), name="resume"),
]
