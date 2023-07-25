from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=256)

    def __str__(self):
         return str(self.category_name)

class Product(models.Model):
    product_name = models.CharField(max_length=512)
    product_desc = models.TextField(blank=True)
    product_price = models.FloatField()
    product_photo = models.ImageField()
    product_amount = models.IntegerField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.product_name)
class Cart(models.Model):
    user_id = models.IntegerField()
    user_products = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_products_amount = models.IntegerField()
    def __str__(self):
        return str(self.user_id)