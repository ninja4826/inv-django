from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.context_processors import csrf

from inventory.models import Product, Location
from inventory.forms import ProductForm

def index(request):
    products_list = Product.objects.order_by('-mpn')[:10]
    context = {'products_list': products_list}
    return render(request, 'inventory/index.html', context)
    
def show(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'inventory/show.html', {'product': product})
    
def delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    if product in Product.objects.all():
        deleted = False
    else:
        deleted = True
    return render(request, 'inventory/delete.html', {'product': product, 'deleted': deleted})

def new_product(request):
    
    c = {}
        
    c.update(csrf(request))
    
    if request.method == 'POST':
        
        form = c['form'] = ProductForm(request.POST)
        
        if form.is_valid():
            new_prod = form.save(commit=False)
            new_prod.save()
            return HttpResponseRedirect('/')
            
    else:
        form = c['form'] = ProductForm()
            
    return render(request, 'inventory/_form.html', c)