from django.db import models
# Create your models here.
class sales(models.Model):
    Item_Weight=models.FloatField(max_length=10,blank=True,null=True,)
    Item_MRP =models.FloatField(max_length=10,blank=True,null=True)
    Item_Visibility=models.FloatField(max_length=10,blank=True,null=True)
    Item_Fat_Content=models.CharField(max_length=10,blank=True,null=True)
    Outlet_location_type=models.CharField(max_length=10,blank=True,null=True)
    Outlet_Type=models.CharField(max_length=10,blank=True,null=True)
    Outlet_Size=models.CharField(max_length=10,blank=True,null=True)
    