from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User

from projects.models import Project
from events.models import Event


# Эта модель хранит в себе записи о существующих географических регионах для Университетов
class Region(models.Model):

    name        = models.CharField(max_length=255)
    is_foreign  = models.IntegerField()

    def __str__(self):
        return self.name
    
# Эта модель хранит список всех Партнёрских университетов
class University(models.Model):

    name    = models.CharField(max_length=255, verbose_name="Название университета-партнёра")
    logo    = models.TextField(verbose_name="???")
    region  = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Территориальное расположение университета-партнёра")

    status  = models.CharField(max_length=15, verbose_name="Статус", choices=(
        (1, 'bachelor'),
        (2, 'master'),
    ), default='bachelor')

    def __str__(self):
        return self.name

# Эта модель хранит список всех студентов на факультете
class Profile(models.Model):

    user                    = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Пользователь", help_text="Каждый пользователь имеет свой profile")

    surname                 = models.CharField(max_length=255, verbose_name="Фамилия студента")
    name                    = models.CharField(max_length=255, verbose_name="Имя студента")
    midname                 = models.CharField(max_length=255, verbose_name="Отчество студента")
    bachelors_start_year    = models.TextField(blank=True, null=True, verbose_name="Дата начала обучения на бакалавра")
    masters_start_year      = models.TextField(blank=True, null=True, verbose_name="Дата начала обучения на магистра")
    university              = models.ForeignKey(University, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Университет, в котором обучается студент")

    projects                = models.ManyToManyField(Project, verbose_name="Проекты")
    groups                  = models.ManyToManyField(Event, verbose_name="События")

    def __str__(self):
        return self.name
    


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
