from django.db import models

# Эта модель под список возможных сфер работы компаний (пример: Маркетинг, IT, Финансы)
class Sphere(models.Model):

    name = models.CharField(max_length=255, verbose_name="Название сферы деятельности")

    def __str__(self):
        return self.name

# Эта модель описывает таблицу содержащую список возможных типов компаний (пример: Малый бизнес, Государственная, Крупный российский бизнес, Крупный зарубежный)
class Type(models.Model):

    name = models.CharField(max_length=255, verbose_name="Название типа компании")

    def __str__(self):
        return self.name
    
# Эта модель описывает таблицу содердащую список всех компаний-партнёров университета
class Company(models.Model):

    name        = models.CharField(max_length=255, verbose_name="Наименование компании")
    type        = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Тип компании")
    sphere      = models.ForeignKey(Sphere, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Сфера работы компании")
    website     = models.TextField(verbose_name="Активный вебсайт компании")

    def __str__(self):
        return self.name

