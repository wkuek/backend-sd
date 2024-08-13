from django.db import models
from backend.constants import *
from cloudinary.models import CloudinaryField
# Create your models here.
class Item(models.Model):
    class Meta(object):
        db_table='item'
    status=models.CharField(
        'status',blank=False,default='draft',max_length=50,db_index=True,choices= STATUS
    )
    name=models.CharField(
        'Name',blank=False,null=False,max_length=120,db_index=True
    )
    category=models.CharField(
        'Categories',blank=False,null=False,max_length=15,db_index=True,default='others',choices=CATEGORIES
    )
    price=models.DecimalField(
        'Price',blank=False,null=False,max_digits=10,decimal_places=2
    )
    image=CloudinaryField(
        'Image',blank=True,null=True,
    )
    created_at=models.DateTimeField(
        'Created at',blank=True,auto_now_add=True
    )
    updated_at=models.DateTimeField(
        'Updated at',blank=True,auto_now=True
    )