from django.db import models

class staff(models.Model):
    Staffname=models.CharField(max_length=50)
    Staffid=models.IntegerField
    Address=models.CharField(max_length=50)
    PanCard= models.CharField(max_length=50)
    AdharcardNo= models.CharField(max_length=50)
    Phno= models.IntegerField

class Vehicle(models.Model):
    VehicleType= models.CharField(max_length=50)
    VehicleNumber=models.IntegerField
    Company=models.CharField(max_length=50)

class Stock(models.Model):
    stock=models.IntegerField
    VehicleNo= models.IntegerField
    Stockid= models.IntegerField

class Bookingbystaff(models.Model):
    Bookingid=models.IntegerField(primary_key=True)
    Stockid=models.IntegerField
    Staffid=models.IntegerField

class Customer(models.Model):
    Custname=models.CharField(max_length=50)
    Custid=models.IntegerField(primary_key=True)
    Address= models.CharField(max_length=50)
    PanCard=models.CharField(max_length=50)
    AdharcardNo= models.CharField(max_length=50)
    PhoneNo=models.IntegerField

class Bookingbycustomer(models.Model):
    custid=models.IntegerField(primary_key=True)
    Stockid= models.IntegerField
    Staffid=models.IntegerField

    
    







    
# Create your models here.
