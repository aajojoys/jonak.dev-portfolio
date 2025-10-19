from django.urls import path

from blog.views import *

urlpatterns = [
    path("", blog_view, name="blog"),
    path("<uuid:blog_id>/", blog_detail_view, name="blog_detail"),
]
