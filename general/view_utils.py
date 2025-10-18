from general.model_utils import *

MENU_KEY = "menu"
LINK_GITHUB_NAME = "github"
LINK_MAIL_NAME = "mail"
LINK_PORTRAIT_NAME = "portrait"

def base_view_add_context_func_helper(context, retrieve_func, keys):
    for key in keys: context[key] = retrieve_func(key)

def base_view_get_contact_link(menu_page, context):
    context[MENU_KEY] = menu_page
    base_view_add_context_func_helper(context, link_get_obj_by_name, [LINK_GITHUB_NAME, LINK_MAIL_NAME, LINK_PORTRAIT_NAME])
    return context
