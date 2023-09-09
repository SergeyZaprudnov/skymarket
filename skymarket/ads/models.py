from django.conf import settings
from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Ad(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название', default='')
    price = models.PositiveIntegerField(verbose_name='Цена', **NULLABLE)
    description = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='ads', **NULLABLE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор',
                               related_name='abs', default=1)
    created_at = models.DateTimeField(verbose_name='Дата и время создания', default=timezone.now)

    def __str__(self):
        result = self.title[:50]
        if len(self.title) > 50:
            result += '...'
        return result

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Comment(models.Model):
    text = models.CharField(max_length=1500, verbose_name='Название', default='')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,  on_delete=models.CASCADE, verbose_name='Автор')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, null=True,  verbose_name='Объявление')
    create_at = models.DateTimeField(verbose_name='Дата и время создания', default=timezone.now)

    def __str__(self):
        result = self.text[:50]
        if len(self.text) > 50:
            result += '...'
        return result

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
