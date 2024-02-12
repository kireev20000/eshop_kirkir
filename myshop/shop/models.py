from django.db import models
from django.urls import reverse

class Category(models.Model):

    name = models.CharField(max_length=200, verbose_name="Категория")
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[ self.slug])

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Товар', )
    slug = models.SlugField(max_length=200, )
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name="Фото")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    description = models.TextField(blank=True, verbose_name='Описание')
    available = models.BooleanField(default=True, verbose_name='Доступность')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано:')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновленно:')

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug',]),
            models.Index(fields=['name',]),
            models.Index(fields=['-created',])
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
