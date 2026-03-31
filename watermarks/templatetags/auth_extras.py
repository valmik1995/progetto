from django import template
from django.contrib.auth.models import Group 

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name): 
    group = Group.objects.get(name=group_name) 
    return True if group in user.groups.all() else False


def upper_tags(tags):
    lista = ['tas', 'nbcr', 'ucl', 'saf', 'sa', 'usar', 'gos', 'coem', 'con']
    if tags in lista:
        tags = tags.upper()
    return tags



