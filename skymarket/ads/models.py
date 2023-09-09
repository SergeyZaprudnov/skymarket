from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Ad(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    price = models.PositiveIntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='ads', **NULLABLE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор',
                               related_name='abs')
    created_at = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        result = self.title[:50]
        if len(self.title) > 50:
            result += '...'
        return result


class Comment(models.Model):
    text = models.CharField(max_length=1500, verbose_name='Описание')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор',
                               related_name='comments')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='Объявление', related_name='comments')
    create_at = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        result = self.text[:50]
        if len(self.text) > 50:
            result += '...'
        return result
