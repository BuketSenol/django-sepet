from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Product(models.Model):
    owner=models.ForeignKey(User, verbose_name=("Satıcı"), on_delete=models.CASCADE)
    name=models.CharField(("Ürün İsmi"), max_length=100)
    content=models.TextField(("Ürün Açıklaması"))
    price=models.IntegerField(("Ürün Fiyatı"))
    image=models.ImageField(("Ürün Resmi"), upload_to="products/")
    slug=models.SlugField(blank=True)
    stock=models.IntegerField(("Ürün Stoku"), default=0, null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name.replace('ı','i'))
        super(Product,self).save(*args, **kwargs)
        
    
    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural="Ürünler"
        verbose_name="Ürün"
        
        
class ShopCard(models.Model):
    owner=models.ForeignKey(User, verbose_name=("Eklayen"), on_delete=models.CASCADE)
    product=models.ForeignKey(Product, verbose_name=("Eklenen Ürün"), on_delete=models.CASCADE)
    count=models.IntegerField(default=1, verbose_name="Adet")
    totalPrice=models.IntegerField(verbose_name="Toplam Fiyat", editable=False) #todo: editable admin panelinden kaybolur
    isPayment=models.BooleanField(default=False, verbose_name="Ödendi mi?")
    created_at=models.DateTimeField( auto_now_add=True)
   
    
    def __str__(self):
        return self.product.name

        
    class Meta:
        verbose_name_plural="Sepetteki Ürünler"
        verbose_name="Sepet"
        
        
    def save(self, *args, **kwargs):
        self.totalPrice = self.product.price * self.count
        super(ShopCard, self).save(*args, **kwargs)
        
class Payment(models.Model):
    owner= models.ForeignKey(User, verbose_name=("Stın alınan"), on_delete=models.CASCADE)
    products = models.ManyToManyField(ShopCard, verbose_name=("Satın alınan Ürünler"))
    totalPrice = models.IntegerField(("Toplam Fiyat"))
    isPayment= models.BooleanField(("Ödendi mi?"), default=False)

    def __str__(self):
        return self.owner.username