from django.db import models
from utils.constants import JOURNAL_TYPES

# Create your models here.

class BookJournalBase(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название")
    price = models.IntegerField(null=False, blank=False, verbose_name="Цена")
    description = models.TextField(max_length=1000, verbose_name="Описание")
    created_at = models.DateField(verbose_name="Дата создания")

    class Meta:
        abstract = False


class Book(BookJournalBase):
    num_pages = models.IntegerField(null=False, blank=False, verbose_name="Количество страниц")
    genre = models.CharField(max_length=255, null=False, blank=False, verbose_name="Жанр")


class Journal(BookJournalBase):
    type = models.SmallIntegerField(choices=JOURNAL_TYPES, null=False, blank=False, verbose_name="Тип")
    publisher = models.CharField(max_length=255, null=False, blank=False, verbose_name="Издатель")