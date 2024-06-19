# groups/views.py

from django.shortcuts import render
from .models import Group

def group_detail(request, group_id):
    group = Group.objects.get(pk=group_id)
    return render(request, 'groups/group_detail.html', {'group': group})
