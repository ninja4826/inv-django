from django.forms import ModelForm
from inventory.models import Product, Location

class ProductForm(ModelForm):
    class Meta:
        model = Product
        
        fields = ['location_name', 'product_name', 'quantity', 'mpn', 'location']