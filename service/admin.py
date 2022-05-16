from django.contrib import admin
from service.models import staff
from service.models import Vehicle
from service.models import Stock
from service.models import Bookingbystaff
from service.models import Customer
from service.models import Bookingbycustomer

class staffAdmin(admin.ModelAdmin):
    list_display1=('Staffname','Staffid','Address','PanCard','AdharcardNo','Phno')

class VehicleAdmin(admin.ModelAdmin):
    list_display2=('VehicleType','VehicleNumber','Company')

class StockAdmin(admin.ModelAdmin):
    list_display3=('stock','VehicleNo','Stockid')

class BookingbystaffAdmin(admin.ModelAdmin):
    list_display4=('Bookingid','Stockid','Staffid')

class CustomerAdmin(admin.ModelAdmin):
    list_display5=('Custname','Custid','Address','PanCard','AdharcardNo','PhoneNo')

class BookingbyCustomerAdmin(admin.ModelAdmin):
    list_display6=('custid','Stockid','Staffid')

admin.site.register(staff,staffAdmin)
admin.site.register(Vehicle,VehicleAdmin)
admin.site.register(Stock,StockAdmin)
admin.site.register(Bookingbystaff,BookingbystaffAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Bookingbycustomer,BookingbyCustomerAdmin)


# Register your models here.
