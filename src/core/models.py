from django.db import models

# Create your models here.
class Company(models.Model):
    pass


class Product(models.Model):

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('title',)
        db_table = 'product'

    company = models.ForeignKey(Company, null=True, on_delate=models.SET_NULL)  # null=True?
    product_name = models.CharField(max_length=200)
    calories = models.IntegerField()
    slug = models.SlugField(unique=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

