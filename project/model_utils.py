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
    stack_obj = model_get_obj(Stack, dictfield)
    return stack_obj.frameworks.all() if stack_obj else []

def project_get_all_attachments_pair():
    project_objs = project_get_all_objs()
    return { obj: project_get_all_attachments(obj) for obj in project_objs }

def project_get_all_category_frameworkds_pair(project_obj):
    framework_objs = project_get_all_frameworks(project_obj)
    category_frameworks_dict = {}
    for obj in framework_objs:
        category_name = obj.category.name
        category_frameworks_dict.setdefault(category_name, [])
        category_frameworks_dict[category_name].append(obj.name)
    return category_frameworks_dict
