from django.db import models
from faker import Faker
from django.utils import timezone

import random
from datetime import date

ukrainian_middle_names = [
    'Петрович', 'Олександрович', 'Олегович', 'Ігорович', 'Володимирович', 'Сергійович', 'Ігорівич', 'Миколаївич',
    'Вікторович', 'Анатолійович', 'Сергійович', 'Андрійович', 'Анатолійович', 'Олексійович', 'Іванович', 'Андріанович',
    'Олександрович', 'Денисович', 'Михайлович', 'Сергійович', 'Андрійович', 'Вікторівич', 'Леонідівна', 'Геннадіївна',
    'Олександрович', 'Нікітівна', 'Тарасівна', 'Павлівна', 'Романович', 'Анжелікович', 'Андріївна', 'Олександрович',
    'Іванович', 'Віталійович', 'Антонович', 'Григоріївна', 'Леонідович', 'Володимирівна', 'Русланович', 'Федорович',
    'Натанович', 'Кирилівна', 'Захарович', 'Ярославівна', 'Мстиславович', 'Даніїлівна', 'Всеволодівна', 'Антінович',
    'Валентинівна', 'Ростиславівна', 'Юрійович', 'Валеріївна', 'Федосіївна', 'Єфремівна', 'Борисович', 'Марківна',
    'Євстахіївна', 'Васильович', 'Олексіївна', 'Савеліївна', 'Мар’янович', 'Євгенович', 'Зеновіївна', 'Всеславівна',
    'Олесьович', 'Андронікович', 'Миронівна', 'Святославівна', 'Давидович', 'Мстиславівна', 'Захарівна', 'Олексійович',
    'Григоріївич', 'Сергійович', 'Левівна', 'Макарович', 'Дмитрович', 'Семенівна', 'Єфросинівна', 'Костянтинівна',
    'Гаврилівна', 'Дорофіївна', 'Андриянівна', 'Вікторівич', 'Соломонівна', 'Варфоломійович', 'Несторович',
    'Вадимівна', 'Афанасіївна', 'Мар’янівна', 'Анікітівна', 'Семіонівна', 'Симонівна', 'Гордіївна', 'Спартаківна',
    'Артемівна', 'Тимофіївна', 'Іларіонівна', 'Аркадіївна', 'Андронімівна', 'Антігонівна', 'Іоаннівна', 'Ізмаїлівна',
    'Казимирівна', 'Ісааківна', 'Герасимівна', 'Даніїлівна', 'Альбертівна', 'Болеславівна', 'Амвросіївна', 'Анісіївна',
    'Вітольдівна', 'Володиславівна', 'Юхимівна', 'Климентівна', 'Корнеліївна', 'Юстиніанівна', 'Агапіївна', 'Глібівна',
    'Горгоніївна', 'Зосимівна', 'Маркелівна', 'Мартінівна', 'Мелентіївна', 'Назаріївна', 'Никифорівна', 'Феодорівна',
    'Філаретівна', 'Іпатіївна', 'Іракліївна', 'Лаврентіївна', 'Лаврінівна', 'Мінаївна', 'Мірілівна', 'Силуанівна',
    'Тихонівна', 'Трифонівна', 'Філімонівна', 'Юліанівна', 'Юріївна', 'Юхиміанівна', 'Юхимович'
]

fake = Faker('uk_UA')


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    room_number = models.IntegerField()

class Position(models.Model):
    position_id = models.AutoField(primary_key=True)
    position_name = models.CharField(max_length=255)
    salary = models.IntegerField()
    bonus_percentage = models.IntegerField()

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=255)
    deadline = models.DateField()
    funding_size = models.IntegerField()

class ProjectExecution(models.Model):
    execution_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    start_date = models.DateField()

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    education = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

# Створюємо відділи
departments = [
    Department(department_name='Програмування', phone_number='123456789', room_number=701),
    Department(department_name='Дизайн', phone_number='987654321', room_number=702),
    Department(department_name='Інформаційні технології', phone_number='555555555', room_number=703),
]
Department.objects.bulk_create(departments)

# Отримуємо створені відділи
departments = Department.objects.all()

# Створюємо посади
positions = [
    Position(position_name='Інженер', salary=50000, bonus_percentage=10),
    Position(position_name='Редактор', salary=60000, bonus_percentage=15),
    Position(position_name='Програміст', salary=70000, bonus_percentage=20),
]
Position.objects.bulk_create(positions)

# Створюємо проекти
projects = [
    Project(project_name='Проект 1', deadline=date(2023, 12, 31), funding_size=100000),
    Project(project_name='Проект 2', deadline=date(2023, 11, 30), funding_size=80000),
    Project(project_name='Проект 3', deadline=date(2023, 12, 31), funding_size=100000),
    Project(project_name='Проект 4', deadline=date(2023, 11, 30), funding_size=40000),
    Project(project_name='Проект 5', deadline=date(2023, 12, 31), funding_size=700000),
    Project(project_name='Проект 6', deadline=date(2023, 11, 30), funding_size=10000),
    Project(project_name='Проект 7', deadline=date(2023, 12, 31), funding_size=200000),
    Project(project_name='Проект 8', deadline=date(2023, 11, 30), funding_size=50000),
    # додайте інші проекти тут
]
Project.objects.bulk_create(projects)



project_executions = []
for project in Project.objects.all():
    department = departments[fake.random_int(0, len(departments) - 1)]
    project_executions.append(ProjectExecution(project=project, department=department, start_date=timezone.now()))

# Додаємо виконання проектів до бази даних
ProjectExecution.objects.bulk_create(project_executions)


def create():
    for _ in range(17):
        employees = [
            Employee(
                last_name=fake.last_name(),
                first_name=fake.first_name(),
                middle_name= random.choice(ukrainian_middle_names),  # Використовуйте для імені по батькові fake.first_name_male()
                address=fake.address(),
                phone_number=fake.phone_number(),
                education=fake.random_element(elements=('Вища', 'Середня')),
                department=departments[fake.random_int(0, len(departments) - 1)],
                position=positions[fake.random_int(0, len(positions) - 1)]
            )
        ]
        Employee.objects.bulk_create(employees)

create()
