from django.forms import ModelForm
from inventory.models import Product, Location
from workorder.models import Workorder, WorkItem

class WorkorderForm(ModelForm):
    class Meta:
        model = Workorder
        
        fields = ['proj_num', 'proj_manager']
        
class WorkItemForm(ModelForm):
    class Meta:
        model = WorkItem
        
        fields = ['product_mpn', 'quantity']