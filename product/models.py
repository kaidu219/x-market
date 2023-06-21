from django.db import models

# Create your models here.


class Unit(models.Model):
    """
    Класс для описания единицы измерения
    """
    title = models.CharField(max_length=100)
    value = models.DecimalField()

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    """
    Класс для описания категорий
    """
    title = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.title


class Subcategory(models.Models):
    """
    Класс для описания подкатегорий
    """
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True, related_name='subcategory')
    title = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    """
    Класс описания товара
    """
    name = models.CharField(max_length=250)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True, related_name='product')
    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE, null=True, blank=True, related_name='product')
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Price(models.Model):
    """
    Класс для описания цены
    """
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='price')
    created_at = models.DateTimeField(auto_created=True)
    start_date = models.DateField()
    duration = models.DurationField()
    value = models.DecimalField()
    is_activa = models.BooleanField()

    def __str__(self) -> str:
        return self.value
