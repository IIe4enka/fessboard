from django.db import models

# Эта модель описывает таблицу содердащую список всех мероприятий, которые проходили на факультете
class Event(models.Model):

    name        = models.CharField(max_length=255, verbose_name="Название мероприятия")
    start       = models.DateField(verbose_name="Дата началы мероприятия")
    end         = models.DateField(verbose_name="Дата конца мероприятия")
    desc        = models.TextField(verbose_name="Описание мероприятия")
    is_frozen   = models.IntegerField(verbose_name="Заморожено ли мероприятие (для тех, которые в процессе планирования\реализации пришлось отложить)")

    def __str__(self):
        return self.name