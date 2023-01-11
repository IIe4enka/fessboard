from django.db import models

#??? 
# [ОТ МИШИ] Это модель под список возможных сфер работы компаний (пример: Маркетинг, IT, Финансы)
class Sphere(models.Model):

    name = models.CharField(max_length=255, verbose_name="???")

    def __str__(self):
        return self.name
    
#???
# [ОТ МИШИ] Это модель описывает таблицу содердащую список возможных типов компаний (пример: Малый бизнес, Государственная, Крупный российский бизнес, Крупный зарубежный)
class Type(models.Model):

    name = models.CharField(max_length=255, verbose_name="???") # Название типа компании

    def __str__(self):
        return self.name
    
#???
# [ОТ МИШИ] Это модель описывает таблицу содердащую список всех компаний-партнёров университета
class Company(models.Model):

    name        = models.CharField(max_length=255, verbose_name="???") # Наименование компании
    type        = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="???") # Тип компании
    sphere      = models.ForeignKey(Sphere, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="???") # Сфера работы компании
    website     = models.TextField(verbose_name="???") # Активный вебсайт компании

    def __str__(self):
        return self.name

#???
# [ОТ МИШИ] Это модель описывает таблицу содердащую список всех мероприятий, которые проходили на факультете
class Event(models.Model):

    name        = models.CharField(max_length=255, verbose_name="???") # Название мероприятия
    start_date  = models.DateField(verbose_name="???") # Дата началы мероприятия
    end_date    = models.DateField(verbose_name="???") # Дата конца мероприятия
    description = models.TextField(verbose_name="???") # Описание мероприятия
    is_frozen   = models.IntegerField(verbose_name="???") # Заморожено ли мероприятие (для тех, которые в процессе планирования\реализации пришлось отложить)

    def __str__(self):
        return self.name
    
#???
# [ОТ МИШИ] Это модель описывает таблицу содердащую список Крупных сфер проектов для каждого Типа проектов (пример: проекты типа Машинное обучение и Анализ данных относятся к сфере Data Science)
class FieldSphere(models.Model):

    name = models.CharField(max_length=255, verbose_name="???") # Наименование сфер проектов

    def __str__(self):
        return self.name















class Groups(models.Model):
    curator_student = models.ForeignKey('Students', on_delete=models.SET_NULL, null=True, blank=True,)

    class Meta:
        managed = False
        db_table = 'groups'

class GroupsInProjects(models.Model):
    project = models.ForeignKey('Projects', on_delete=models.SET_NULL, null=True, blank=True,)
    group = models.ForeignKey(Groups, on_delete=models.SET_NULL, null=True, blank=True,)

    class Meta:
        managed = False
        db_table = 'groups_in_projects'

class ManagersInEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True,)
    student = models.ForeignKey('Students', on_delete=models.SET_NULL, null=True, blank=True,)

    class Meta:
        managed = False
        db_table = 'managers_in_Event'

class ManagersInProjects(models.Model):
    project = models.ForeignKey('Projects', on_delete=models.SET_NULL, null=True, blank=True,)
    student = models.ForeignKey('Students', on_delete=models.SET_NULL, null=True, blank=True,)

    class Meta:
        managed = False
        db_table = 'managers_in_projects'

class ParticipantsInEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True,)
    student = models.ForeignKey('Students', on_delete=models.SET_NULL, null=True, blank=True,)

    class Meta:
        managed = False
        db_table = 'participants_in_Event'

class ProjectFields(models.Model):
    field_id = models.AutoField(primary_key=True)
    field = models.CharField(max_length=255)
    sphere = models.ForeignKey("FieldSphere", on_delete=models.SET_NULL, null=True, blank=True,)

    class Meta:
        managed = False
        db_table = 'project_fields'


class ProjectGrades(models.Model):
    grade_id = models.AutoField(primary_key=True)
    grade = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'project_grades'

class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=255)
    project_description = models.TextField()
    project_result = models.TextField()
    is_frozen = models.IntegerField()
    project_start_date = models.DateField()
    project_end_date = models.DateField()
    project_grade = models.ForeignKey(ProjectGrades, on_delete=models.SET_NULL, null=True, blank=True,)
    project_field = models.ForeignKey(ProjectFields, on_delete=models.SET_NULL, null=True, blank=True,)
    project_company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True,)
    project_dateadded = models.DateTimeField(db_column='project_dateAdded', blank=True,
                                             null=True)  # Field name made lowercase.
    project_dateupdated = models.DateTimeField(db_column='project_dateUpdated', blank=True,
                                               null=True)  # Field name made lowerca

    class Meta:
        managed = False
        db_table = 'projects'

class Regions(models.Model):
    region_id = models.AutoField(primary_key=True)
    region = models.CharField(max_length=255)
    is_foreign = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'regions'

class StudentStatuses(models.Model):
    student_status_id = models.AutoField(primary_key=True)
    student_status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'student_statuses'

class Students(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_surname = models.CharField(max_length=255)
    student_name = models.CharField(max_length=255)
    student_midname = models.CharField(max_length=255)
    bachelors_start_year = models.TextField(blank=True,
                                            null=True)  # This field type is a guess.
    masters_start_year = models.TextField(blank=True,
                                          null=True)  # This field type is a guess.
    student_status = models.ForeignKey(StudentStatuses, on_delete=models.SET_NULL, null=True, blank=True,)
    bachelors_university = models.ForeignKey('Universities', on_delete=models.SET_NULL, null=True, blank=True,)
    masters_university = models.ForeignKey('Universities', on_delete=models.SET_NULL, null=True, blank=True, related_name='Uni_masters')

    class Meta:
        managed = False
        db_table = 'students'


class StudentsInGroups(models.Model):
    group = models.ForeignKey(Groups, on_delete=models.SET_NULL, null=True, blank=True,)
    student = models.ForeignKey(Students, on_delete=models.SET_NULL, null=True, blank=True,)

    class Meta:
        managed = False
        db_table = 'students_in_groups'

class Teachers(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    teacher_surname = models.CharField(max_length=255)
    teacher_name = models.CharField(max_length=255)
    teacher_midname = models.CharField(max_length=255)
    teacher_university = models.ForeignKey('Universities', on_delete=models.SET_NULL, null=True, blank=True,)

    class Meta:
        managed = False
        db_table = 'teachers'


class TeachersInEvent(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.SET_NULL, null=True, blank=True,)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True,)

    class Meta:
        managed = False
        db_table = 'teachers_in_Event'

class TeachersInProjects(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.SET_NULL, null=True, blank=True,)
    project = models.ForeignKey(Projects, on_delete=models.SET_NULL, null=True, blank=True,)

    class Meta:
        managed = False
        db_table = 'teachers_in_projects'

class Universities(models.Model):
    university_id = models.AutoField(primary_key=True)
    university_name = models.CharField(max_length=255)
    university_logo = models.TextField()
    university_region = models.ForeignKey(Regions, on_delete=models.SET_NULL, null=True, blank=True,)

    class Meta:
        managed = False
        db_table = 'universities'
