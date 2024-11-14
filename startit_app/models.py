from django.db import models
from pytils.translit import slugify
from datetime import datetime
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField("Название областей", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    class Meta:
        verbose_name = "Область"
        verbose_name_plural = "Области"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Job(models.Model):
    title = models.CharField("Название курса", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Выберите область")
    company = models.CharField("Название компании", max_length=100)
    expirience = models.CharField("Срок курса", max_length=80, default="не указано")
    salary = models.CharField("Стоимость курса", max_length=50)
    description = models.TextField("Описание курса")
    skills = models.CharField("Будущие навыки", max_length=255)
    address = models.CharField("Адрес", max_length=100, default="Алматы, Абая 52г")
    phone = models.CharField("Телефон", max_length=15)
    email = models.CharField("E-mail", max_length=100)
    created_at = models.DateTimeField("Дата и время публикации курса", default=datetime.now)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title

class Guide(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    description = models.TextField("Описание гайда")
    image = models.CharField("URL-фото", max_length=500)
    created_at = models.DateTimeField("Дата и время публикации", default=datetime.now)

    class Meta:
        verbose_name = "Гайд"
        verbose_name_plural = "Гайды"

    def __str__(self):
        return self.title


class Test(models.Model):
    title = models.CharField("Название задания", max_length=255)
    #cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Выберите область", default="1")  # Укажите значение по умолчанию
    tsar = models.CharField("Цель", max_length=100)
    description = models.TextField("Описание задания")
    task = models.CharField("задание", max_length=255)
    answer = RichTextField("ответ")
    author = models.CharField("Автор", max_length=100, default="Не указан")
    created_at = models.DateTimeField("Дата и время публикации курса", default=datetime.now)

    class Meta: 
        verbose_name = "Задание" 
        verbose_name_plural = "Задания" 
    def __str__(self): 
        return self.title
    