from django.conf import settings

from blog.model_utils import *

HTML_PAGEBREAK = "<br>"
TAGNAME_IMG = "img"
TAGNAME_DIV = "div"
TAGNAME_ELEM_SOURCE = "src"
TAGNAME_ELEM_CLASS = "class"
SELFCLOSING_TAGNAME_LIST = [TAGNAME_IMG, 'input', 'meta', 'link']

DEFAULT_CLASS_IMG = "content-img"
DEFAULT_CLASS_NORMAL = "desc"
DEFAULT_CLASS_IMGDIV = "content-img-div"

def blogitem_get_content(blogitem_obj):
    """
    Construct content with corresponding HTML tag & attributes

    Args:
        blogitem_obj (query obj): object from BlogItem model
    Returns:
        (str): formatted content

    """
    content = ""
    if not blogitem_obj.is_custom:
        content += f"<{blogitem_obj.tag_name}"
        attr_dict = blogitem_obj.attr_value
        is_img = blogitem_obj.tag_name == TAGNAME_IMG
        is_default = blogitem_obj.is_default
        if blogitem_obj.is_default:
            attr_dict.setdefault("class", "")
            if is_img:
                attr_dict.setdefault(TAGNAME_ELEM_SOURCE, "")
                attr_dict['class'] += f" {DEFAULT_CLASS_IMG}"
            else:
                attr_dict['class'] += f" {DEFAULT_CLASS_NORMAL}"

        for key, val in attr_dict.items():
            if (key == TAGNAME_ELEM_SOURCE) and (blogitem_obj.attachment):
                content += f' {key}="{settings.MEDIA_URL}/{blogitem_obj.attachment}" '
            else:
                content += f' {key}="{val}" '
        content += f">{blogitem_obj.content}"
        if blogitem_obj.tag_name not in SELFCLOSING_TAGNAME_LIST:
            content += f"</{blogitem_obj.tag_name}>"

        if is_default and is_img: content = f"<{TAGNAME_DIV} class='{DEFAULT_CLASS_NORMAL} {DEFAULT_CLASS_IMGDIV}'>{content}</{TAGNAME_DIV}>"
    else:
        content = blogitem_obj.content
    return content

def blog_get_all_contents(blog_obj):
    blogitem_objs = blogitem_get_objs_by_blog(blog_obj)
    content = ""
    # TODO: add DOM (add div with particular css style for paragraphing)
    for item in blogitem_objs:
        content += HTML_PAGEBREAK
        content += blogitem_get_content(item)
    return content
