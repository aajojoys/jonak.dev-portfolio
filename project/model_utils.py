from utility.model_utils import *
from project.models import *

def project_get_obj(pk):
    dictfield = dict(pk=pk)
    return model_get_obj(Project, dictfield)

def project_get_all_objs():
    return model_get_all_objs(Project)

def project_get_all_attachments(project_obj):
    dictfield = dict(project=project_obj)
    return model_get_filter_objs(dictfield, Model=ProjectAttachment)

def project_get_all_frameworks(project_obj):
    dictfield = dict(project=project_obj)
    return model_get_filter_objs(dictfield, Model=Stack)

def project_get_all_attachments_pair():
    project_objs = project_get_all_objs()
    return { obj: project_get_all_attachments(obj) for obj in project_objs }
