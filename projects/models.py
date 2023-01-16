from django.db import models
from django.utils.timezone import now
from company.models import Company


# Эта модель описывает таблицу содержащую список Крупных сфер проектов для каждого Типа проектов (пример: проекты типа Машинное обучение и Анализ данных относятся к сфере Data Science)
class Sphere(models.Model):

    name = models.CharField(max_length=255, verbose_name="Наименование сфер проектов")

    def __str__(self):
        return self.name

# Эта таблица хранит в себе список Типов проектов, а также информацию о том к какой Сфере относится Тип проекта. Это нужна для сбора статистики по направлениям проектов
class Type(models.Model):

    name    = models.CharField(max_length=255)
    sphere  = models.ForeignKey(Sphere, on_delete=models.SET_NULL, null=True, blank=True,)

    def __str__(self):
        return self.name

# Эта модель отражает список Грейдов (уровней сложности) проектов
class Grade(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Эта модель хранит в себе записи о всех проектах
class Project(models.Model):

    name        = models.CharField(max_length=255)
    desc        = models.TextField()
    result      = models.TextField()
    is_frozen   = models.IntegerField()
    start       = models.DateField()
    end         = models.DateField()
    grade       = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True, blank=True,)
    field       = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True,)
    company     = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True,)

    created     = models.DateTimeField(default=now)
    updated     = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.updated = now()
        return super(Project, self).save(*args, **kwargs)