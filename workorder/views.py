from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.context_processors import csrf
from django.forms.models import inlineformset_factory

from inventory.models import Product, Location
from workorder.models import Workorder, WorkItem


def edit_work_items(request, workorder_id):
    
    workorder = Workorder.objects.get(pk=workorder_id)
    
    WorkInlineFormSet = inlineformset_factory(Workorder, WorkItem, extra=1)
    
    c = {}
    
    c.update(csrf(request))
    
    if request.method == 'POST':
        formset = c['formset'] = WorkInlineFormSet(request.POST, request.FILES, instance=workorder)
        
        if formset.is_valid():
            work_item = formset.save(commit=False)
            work_item.save()
            return HttpResponseRedirect(workorder.get_absolute_url())
    else:
        formset = c['formset'] = WorkInlineFormSet(instance=workorder)
    
    return render(request, 'workorder/_edit_workitems.html', c)