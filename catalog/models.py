from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(**NULLABLE)
    img = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Превью')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price_per_purchase = models.IntegerField(**NULLABLE, verbose_name='Цена за покупку')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания', **NULLABLE)
    updated_at = models.DateField(auto_now=True, verbose_name='Дата изменения', **NULLABLE)

    def __str__(self):
        return f'{self.name} в категории {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):

    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(**NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
