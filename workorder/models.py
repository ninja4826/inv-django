from django.db import models

from inventory.models import Product, Location

class Workorder(models.Model):
    proj_num = models.CharField(max_length=200)
    proj_manager = models.CharField(max_length=200)
    
class WorkItem(models.Model):
    product_mpn = models.CharField(max_length=200)
    product = models.ForeignKey(Product)
    workorder = models.ForeignKey(Workorder)
    
    quantity = models.IntegerField(default=1)
    
    def save(self, *args, **kwargs):
        prod = Product.objects.get(mpn=self.product_mpn)
        
        self.product = prod
        
        super(WorkItem, self).save(*args, **kwargs)
        
