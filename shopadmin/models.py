from django.db import models

# Create your models here.
class Shop(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    imageUrl = models.ImageField(upload_to='shop_images/')

    def __str__(self):
        return self.title

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    description = models.TextField()
    title = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    price = models.FloatField()
    images = models.JSONField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
