from django.shortcuts import render

from general.model_utils import *
from general.view_utils import *

# Create your views here.
MENU_ABOUT = "about"
STATEMENT_ABOUT_TITLE_NAME = "about_title"
STATEMENT_ABOUT_NAME = "about"
STATEMENT_CONTACT_NAME = "contact"

def about_view(request):
    context = {}
    base_view_get_contact_link(MENU_ABOUT, context)
    base_view_add_context_func_helper(context, statement_get_obj_by_name, [STATEMENT_ABOUT_TITLE_NAME, STATEMENT_ABOUT_NAME, STATEMENT_CONTACT_NAME])
    return render(request, "about.html", context)
