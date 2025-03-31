from django.core.validators import MaxValueValidator
from django.db import models

from users.models import User


class Contacts(models.Model):
    email = models.EmailField(verbose_name="Почта")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house_number = models.PositiveIntegerField(validators=[MaxValueValidator(500)], verbose_name="Номер дома")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    model = models.CharField(max_length=255, verbose_name="Модель продукта")
    release_date = models.DateField(verbose_name="Дата выхода на рынок")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class NetworkNode(models.Model):
    FACTORY = "factory"
    RETAIL = "retail"
    ENTREPRENEUR = "entrepreneur"
    LEVEL_CHOICES = (
        (FACTORY, "Завод"),
        (RETAIL, "Розничная сеть"),
        (ENTREPRENEUR, "Индивидуальный предприниматель"),
    )

    name = models.CharField(max_length=255, verbose_name="Название")
    level = models.CharField(max_length=30, choices=LEVEL_CHOICES, verbose_name="Уровень звена")
    contacts = models.ForeignKey(Contacts, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Контакты")
    products = models.ManyToManyField(Product, verbose_name="Продукты")  # Но для простоты, можно использовать JSON
    supplier = models.ForeignKey("self", on_delete=models.PROTECT, blank=True, null=True,
                                 related_name="before_supplier", verbose_name="Поставщик")
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Задолженность")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сеть"
        verbose_name_plural = "Сети"
