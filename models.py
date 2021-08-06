#from django.db import models
from django.db import models
class booking(models.Model):
    firstname = models.CharField(max_length=200)
    middlename = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
  #  address = models.CharField(max_length=200)
   # phonenumber = models.CharField(max_length=200)

    def __str__(self):
        return self.firstname
class slot(models.Model):
    address=models.ForeignKey(booking,on_delete=models.CASCADE)
    phonenumber=models.CharField(max_length=500)
    rating=models.CharField(max_length=500)
    def __str__(self):
        return self.address


# Create your models here.
