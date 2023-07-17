from django.db import models
from django.urls import reverse


class Notes(models.Model):
    objects = None
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Заметка')
    date = models.DateTimeField('Дата', auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note', kwargs={'note_id': self.pk})

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'


class Category(models.Model):
    name = models.CharField('Название', max_length=50, db_index=True)

    def __str__(self):
        return self.name
