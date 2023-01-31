import random

from django.db import models
from django.db.models import Q
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
import re
from .validators import validate_address_length, check_experience
# Create your models here.


class BasePerson(models.Model):
    class PersonGenderChoice(models.IntegerChoices):
        MALE = 1, 'Мужской'
        FEMALE = 0, 'Женский'
        __empty__ = 'Не определено'

    name = models.CharField(verbose_name='Имя', max_length=255,
                            blank=True, null=True,
                            validators=[RegexValidator(
                                regex='^\D+$',
                                message='Введите строку',
                                flags=re.IGNORECASE,
                            )])
    age = models.IntegerField(verbose_name='Возраст', default=1,
                              blank=True, null=True)
    gender = models.BooleanField(verbose_name='Пол', default=PersonGenderChoice.MALE,
                                 choices=PersonGenderChoice.choices,
                                 blank=True, null=True)

    address = models.CharField(verbose_name='Адрес', max_length=255,
                               blank=True, null=True,
                               validators=[validate_address_length])

    id = models.IntegerField(editable=False, primary_key=True)

    def save(self, *args, **kwargs):
        '''if self.name == 'Irod':
            return
        else:
            super().save(*args, **kwargs)'''
        if self.name:
            self.id = f'{random.randint(1, 10000000000)}'
            super().save(*args, **kwargs)


    class Meta:
        abstract = True

class Person(BasePerson):

    NAME_TERMS_CHOICES = [
        ('Basic', (
            ('mr', 'Mr'),
            ('ms', 'Ms'),
        )
        ),
        ('Prof', (
            ('dr', 'Dr'),
            ('sir', 'Sir'),
        )),
        ('unknown', 'Unknown')
    ]

    name_terms = models.CharField(verbose_name='',
                                  default=NAME_TERMS_CHOICES[1][1],
                                  choices=NAME_TERMS_CHOICES,
                                  max_length=255)
    experience = models.IntegerField(verbose_name='Опыт работы', validators=[check_experience])

    def get_absolute_url(self):
        return f'/human/person/{self.pk}'

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

        ordering = ['pk', ]
        get_latest_by = ['-age', ]

        constraints = [
            models.CheckConstraint(check=models.Q(age__gte=16), name='age'),
        ]

class Child(BasePerson):

    parent_field = models.ManyToManyField(Person, through='PersonsRelationShip')

    age = models.IntegerField(verbose_name='Возраст', default=1,
                              blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(15)])

    class Meta:
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'

class PersonsRelationShip(models.Model):
    parent = models.ForeignKey(Person, on_delete=models.CASCADE)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Родитель: {self.parent} - Ребенок: {self.child}'

    class Meta:
        verbose_name = 'Отношения'
        verbose_name_plural = 'Отношения'
        unique_together = ['child', ]