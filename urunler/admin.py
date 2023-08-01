from django.contrib import admin
from .models import*


class ProductAdmin(admin.ModelAdmin):
    list_display = ['owner', 'name','price']
    list_filter=['owner__username']
    readonly_fields =['slug']
    
class CardAdmin(admin.ModelAdmin):
    list_display=['owner', 'product','totalPrice','created_at']
    readonly_fields=['totalPrice','created_at'] #todo: sadece okunabilir alan ekler değiştirilemez
    
    
    

admin.site.register(Product, ProductAdmin) #todo:Önceki model sonraki class
admin.site.register(ShopCard,CardAdmin )
admin.site.register(Payment)