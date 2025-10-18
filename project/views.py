from django.shortcuts import render

from general.model_utils import statement_get_obj_by_name
from general.view_utils import base_view_add_context_func_helper, base_view_get_contact_link
from project.model_utils import *

MENU_PROJECT = "project"
STATEMENT_PROJECT_TITLE = "project_title"
STATEMENT_PROJECT_TITLE_DESC = "project_title_desc"
PROJECT_ATTACHMENTS_DICT = "project_attachments"
STATEMENT_PROJECT_DETAIL_TITLE = "project_detail_title"
PROJECT_ITEM = "project"
IMAGE_ITEMS = "images"
FRAMEWORK_ITEMS = "frameworks"
CATEGORY_FRAMEWORKS_DICT = "category_frameworks"

# Create your views here.
def project_view(request):
    context = {}
    base_view_get_contact_link(MENU_PROJECT, context)
    context[PROJECT_ATTACHMENTS_DICT] = project_get_all_attachments_pair()
    base_view_add_context_func_helper(context, statement_get_obj_by_name, [STATEMENT_PROJECT_TITLE, STATEMENT_PROJECT_TITLE_DESC])
    return render(request, "project.html", context)

def project_detail_view(request, project_id):
    context = {}
    base_view_get_contact_link(MENU_PROJECT, context)
    project_obj = project_get_obj(project_id)
    context[STATEMENT_PROJECT_DETAIL_TITLE] = statement_get_obj_by_name(STATEMENT_PROJECT_DETAIL_TITLE)
    context[PROJECT_ITEM] = project_obj
    context[IMAGE_ITEMS] = project_get_all_attachments(project_obj)
    context[CATEGORY_FRAMEWORKS_DICT] = project_get_all_category_frameworkds_pair(project_obj)
    return render(request, "project_detail.html", context)
