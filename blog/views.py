from django.shortcuts import render
from blog.view_utils import blog_get_all_contents

from general.model_utils import statement_get_obj_by_name
from general.view_utils import *
from blog.model_utils import *

MENU_BLOG = "blog"
BLOG_ATTACHMENTS_DICT = "blog_attachments"
STATEMENT_BLOG_TITLE = "blog_title"
STATEMENT_BLOG_TITLE_DESC = "blog_title_desc"
STATEMENT_BLOG_DETAIL_TITLE = "blog_detail_title"
BLOG_ITEM = "blog"
IMAGE_ITEMS = "images"
BLOG_ATTACHMENTS_DICT = "blog_attachments"
BLOG_CONTENTS = "blog_contents"

# Create your views here.
def blog_view(request):
    context = {}
    base_view_get_contact_link(MENU_BLOG, context)
    context[BLOG_ATTACHMENTS_DICT] = blog_get_all_attachments_pair()
    base_view_add_context_func_helper(context, statement_get_obj_by_name, [STATEMENT_BLOG_TITLE, STATEMENT_BLOG_TITLE_DESC])
    return render(request, "blog.html", context)

def blog_detail_view(request, blog_id):
    context = {}
    base_view_get_contact_link(MENU_BLOG, context)
    blog_obj = blog_get_obj(blog_id)
    context[STATEMENT_BLOG_DETAIL_TITLE] = statement_get_obj_by_name(STATEMENT_BLOG_DETAIL_TITLE)
    context[BLOG_ITEM] = blog_obj
    context[IMAGE_ITEMS] = blog_get_all_attachments(blog_obj)
    context[BLOG_CONTENTS] = blog_get_all_contents(blog_obj)
    return render(request, "blog_detail.html", context)
