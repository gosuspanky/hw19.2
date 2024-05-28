from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(**NULLABLE)
    img = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Превью')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price_per_purchase = models.IntegerField(**NULLABLE, verbose_name='Цена за покупку')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания', **NULLABLE)
    updated_at = models.DateField(auto_now=True, verbose_name='Дата изменения', **NULLABLE)

    owner = models.ForeignKey(User, verbose_name="Владелец", help_text="Укажите владельца", **NULLABLE,
                              on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'

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


class Blog(models.Model):
    name = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(**NULLABLE, max_length=250, verbose_name='slug')
    content = models.TextField(**NULLABLE, verbose_name='содержимое')
    img = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Превью')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания', **NULLABLE)
    is_published = models.BooleanField(**NULLABLE, default=True, verbose_name='Признак публикации')
    views_count = models.IntegerField(**NULLABLE, default=0, verbose_name='Счетчик просмотров')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'


class Version(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='versions')
    version_num = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(**NULLABLE, max_length=100, verbose_name='название версии')
    is_active_version = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
