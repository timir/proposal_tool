from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    telephone = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Mall(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City)
    
    def __str__(self):
        return self.name  
        
class Proposal(models.Model):
    client_name = models.ForeignKey(Client)
    created_date = models.DateTimeField(default=timezone.now)

  
    def __str__(self):
        return str(self.client_name)
        
class Item(models.Model):
    client_name = models.ForeignKey(Proposal, default=0)
    city_name = models.ForeignKey(City)
    mall_name = models.ForeignKey(Mall)
    location = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    rates = models.IntegerField(default=0)
    remark = models.TextField()
    
    def __str__(self):
        return str(self.city_name)
        
        
class AvailableDate(models.Model):
    client_name = models.ForeignKey(Item, default=0)
    available_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.client_name)
    
    

            
    
    
    


