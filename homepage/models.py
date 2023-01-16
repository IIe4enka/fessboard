from django.db import models


# Эта модель под список возможных сфер работы компаний (пример: Маркетинг, IT, Финансы)
class Sphere(models.Model):

    name = models.CharField(max_length=255, verbose_name="???")

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


# Эта модель описывает таблицу содердащую список всех мероприятий, которые проходили на факультете
class Event(models.Model):

    name        = models.CharField(max_length=255, verbose_name="Название мероприятия")
    start_date  = models.DateField(verbose_name="Дата началы мероприятия")
    end_date    = models.DateField(verbose_name="Дата конца мероприятия")
    description = models.TextField(verbose_name="Описание мероприятия")
    is_frozen   = models.IntegerField(verbose_name="Заморожено ли мероприятие (для тех, которые в процессе планирования\реализации пришлось отложить)")

    def __str__(self):
        return self.name
    
# Эта модель описывает таблицу содердащую список Крупных сфер проектов для каждого Типа проектов (пример: проекты типа Машинное обучение и Анализ данных относятся к сфере Data Science)
class FieldSphere(models.Model):

    name = models.CharField(max_length=255, verbose_name="Наименование сфер проектов")

    def __str__(self):
        return self.name




# ???
class Region(models.Model):
    name        = models.CharField(max_length=255)
    is_foreign  = models.IntegerField()

    def __str__(self):
        return self.name
    
#???
class University(models.Model):
    name    = models.CharField(max_length=255, verbose_name="???")
    logo    = models.TextField(verbose_name="???")
    region  = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="???")









class Groups(models.Model):

    students = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="???")

    def __str__(self):
        return self.id


# ???
class Student(models.Model):

    surname                 = models.CharField(max_length=255, verbose_name="???")
    name                    = models.CharField(max_length=255, verbose_name="???")
    midname                 = models.CharField(max_length=255, verbose_name="???")
    bachelors_start_year    = models.TextField(blank=True, null=True, verbose_name="???")
    masters_start_year      = models.TextField(blank=True, null=True, verbose_name="???")  # This field type is a guess.

    student_status          = models.ForeignKey(StudentStatus, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="???")
    bachelors               = models.ForeignKey(University, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="???")
    masters                 = models.ForeignKey(University, on_delete=models.SET_NULL, null=True, blank=True, related_name='Uni_masters', verbose_name="???")


class StudentsInGroups(models.Model):
    group = models.ForeignKey(Groups, on_delete=models.SET_NULL, null=True, blank=True,)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True,)

    class Meta:
        managed = False
        db_table = 'students_in_groups'











# Эта модель не нужна ???. В теории она должна была быть ManyToMany связью между Group и Project таблицами
class GroupsInProjects(models.Model):
    project = models.ForeignKey('Projects', on_delete=models.SET_NULL, null=True, blank=True,)
    group = models.ForeignKey(Groups, on_delete=models.SET_NULL, null=True, blank=True,)

    class Meta:
        managed = False
        db_table = 'groups_in_projects'


# Эта таблица отражает ManyToMany связь между Проектными менеджерами и Мероприятиями. Здесь указаны все Менеджеры во всех мероприятиях.
class ManagersInEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True,)
    student = models.ForeignKey('Students', on_delete=models.SET_NULL, null=True, blank=True,)

    class Meta:
        managed = False
        db_table = 'managers_in_Event'


# Эта таблица отражает ManyToMany связь между Проектными менеджерами и Проектами. Здесь указаны все Менеджеры во всех проектах
class ManagersInProjects(models.Model):
    project = models.ForeignKey('Projects', on_delete=models.SET_NULL, null=True, blank=True,)
    student = models.ForeignKey('Students', on_delete=models.SET_NULL, null=True, blank=True,)

    class Meta:
        managed = False
        db_table = 'managers_in_projects'


# Эта таблица отражает ManyToMany связь между Участниками (студентами) и Мероприятиями. Здесь указаны все Участники во всех Мероприятиях
class ParticipantsInEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True,)
    student = models.ForeignKey('Students', on_delete=models.SET_NULL, null=True, blank=True,)

    class Meta:
        managed = False
        db_table = 'participants_in_Event'


# Эта таблица хранит в себе список Типов проектов, а также информацию о том к какой Сфере относится Тип проекта. Это нужна для сбора статистики по направлениям проектов
class ProjectFields(models.Model):
    field_id = models.AutoField(primary_key=True)
    field = models.CharField(max_length=255)
    sphere = models.ForeignKey("FieldSphere", on_delete=models.SET_NULL, null=True, blank=True,)

    class Meta:
        managed = False
        db_table = 'project_fields'


# Эта модель отражает список Грейдов (уровней сложности) проектов
class ProjectGrades(models.Model):
    grade_id = models.AutoField(primary_key=True)
    grade = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'project_grades'


# Эта модель хранит в себе записи о всех проектах
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


# Эта модель хранит в себе записи о существующих географических регионах для Университетов
class Regions(models.Model):
    region_id = models.AutoField(primary_key=True)
    region = models.CharField(max_length=255)
    is_foreign = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'regions'


# Эта модель хранит в себе список всех статусов студентов (например: Учится, Отчислен, В академе)
class StudentStatuses(models.Model):
    student_status_id = models.AutoField(primary_key=True)
    student_status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'student_statuses'


# Эта модель хранит список всех студентов на факультете
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



# Эта модель не нужна ??? Она в теории должна была отражать ManyToMany связь между Student и Group, учитывать всех студентов во всех группах
class StudentsInGroups(models.Model):
    group = models.ForeignKey(Groups, on_delete=models.SET_NULL, null=True, blank=True,)
    student = models.ForeignKey(Students, on_delete=models.SET_NULL, null=True, blank=True,)

    class Meta:
        managed = False
        db_table = 'students_in_groups'


# Эта модель хранит список всех преподавателей на факультете
class Teachers(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    teacher_surname = models.CharField(max_length=255)
    teacher_name = models.CharField(max_length=255)
    teacher_midname = models.CharField(max_length=255)
    teacher_university = models.ForeignKey('Universities', on_delete=models.SET_NULL, null=True, blank=True,)

    class Meta:
        managed = False
        db_table = 'teachers'


# Преподаватели в мероприятиях. ManyToMany
class TeachersInEvent(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.SET_NULL, null=True, blank=True,)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True,)

    class Meta:
        managed = False
        db_table = 'teachers_in_Event'


# Преподаватели в проектах. ManyToMany
class TeachersInProjects(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.SET_NULL, null=True, blank=True,)
    project = models.ForeignKey(Projects, on_delete=models.SET_NULL, null=True, blank=True,)

    class Meta:
        managed = False
        db_table = 'teachers_in_projects'