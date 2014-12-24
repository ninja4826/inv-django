import datetime, re

from django.db import models
from django.forms import ModelForm


class Location(models.Model):
    
    
    isle = models.CharField(max_length=3)
    segment = models.CharField(max_length=3)
    shelf = models.CharField(max_length=3)
    box = models.CharField(max_length=3)
    location_name = models.CharField(max_length=12, default="")
    
    def __str__(self):
        return (self.isle + self.segment + self.shelf + self.box)
    
    
class Product(models.Model):
    
    
    location_name = models.CharField(max_length=12)
    product_name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    mpn = models.CharField(max_length=200)
    
    location = models.ForeignKey(Location)
    
    def add(self, increment):
        self.quantity += increment
        
    def set_location(self):
        s = self.location_name
        str_arr = []
        num_arr = []
        
        str_locations = [[m.start(0), m.end(0)] for m in re.finditer('[a-zA-Z]', s)]
        
        for str_location in str_locations:
            str_arr.append(s[str_location[0]])
        
        temp_arr = []
        for val in range(str_locations[0][1], str_locations[1][0]):
            temp_arr.append(s[val])
        
        num_arr.append(''.join(temp_arr))
        temp_arr = []
        for val in range(str_locations[1][1], len(s)):
            temp_arr.append(s[val])
        
        num_arr.append(''.join(temp_arr))
        
        id_arr = [str_arr[0], num_arr[0], str_arr[1], num_arr[1]]
        
        return {'isle': id_arr[0], 'segment': id_arr[1], 'shelf': id_arr[2], 'box': id_arr[3], 'name': s}
        
    def save(self, *args, **kwargs):
        attrs = self.set_location()
        
        self.location = Location.objects.get_or_create(
            location_name = attrs['name'],
            isle = attrs['isle'],
            segment = attrs['segment'],
            shelf = attrs['shelf'],
            box = attrs['box'])[0]
            
        super(Product, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.mpn
        


