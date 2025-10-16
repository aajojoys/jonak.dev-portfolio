from utility.model_utils import *
from blog.models import *

def blog_get_obj(pk):
    dictfield = dict(pk=pk)
    return model_get_obj(Blog, dictfield)

def blog_get_all_objs():
    return model_get_all_objs(Blog)

def blog_get_all_attachments(blog_obj):
    dictfield = dict(blog=blog_obj)
    return model_get_filter_objs(dictfield, Model=BlogAttachment)

def blog_get_all_attachments_pair():
    blog_objs = blog_get_all_objs()
    return { obj: blog_get_all_attachments(obj) for obj in blog_objs }

def blogitem_get_objs_by_blog(blog_obj):
    dictfield = dict(blog=blog_obj)
    return model_get_filter_objs(dictfield, Model=BlogItem).order_by('order')
