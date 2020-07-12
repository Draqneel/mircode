from datetime import timedelta

from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=100, verbose_name="Отчество")

    def get_full_name(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    def __str__(self):
        return self.get_full_name()


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField(max_length=255, verbose_name="Название")
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class PurchaseRequest(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Книга")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    phone = models.CharField(max_length=25, verbose_name="Телефон")
    comment = models.CharField(max_length=255, default='', verbose_name="Комментарий", blank=True)
    created_date = models.DateTimeField(default=timezone.now(), verbose_name="Дата создания")

    def __str__(self):
        return f'{self.user.username} - {self.book.title}'

    def save(self, *args, **kwargs):
        self.created_date += timedelta(hours=3)
        return super(PurchaseRequest, self).save(*args, **kwargs)
