from utility.model_utils import *
from general.models import *

def link_get_all_objs():
    return model_get_all_objs(Link)

def link_get_obj_by_name(name):
    dictfield = dict(name=name)
    return model_get_obj(Link, dictfield)

def statement_get_obj_by_name(name):
    dictfield = dict(name=name)
    return model_get_obj(Statement, dictfield)
