# Generated by Django 4.1.5 on 2023-01-31 10:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import person.validators
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.RegexValidator(flags=re.RegexFlag['IGNORECASE'], message='Введите строку', regex='^\\D+$')], verbose_name='Имя')),
                ('gender', models.BooleanField(blank=True, choices=[(None, 'Не определено'), (1, 'Мужской'), (0, 'Женский')], default=1, null=True, verbose_name='Пол')),
                ('address', models.CharField(blank=True, max_length=255, null=True, validators=[person.validators.validate_address_length], verbose_name='Адрес')),
                ('experience', models.IntegerField(validators=[person.validators.check_experience], verbose_name='Опыт работы')),
                ('age', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(15)], verbose_name='Возраст')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.RegexValidator(flags=re.RegexFlag['IGNORECASE'], message='Введите строку', regex='^\\D+$')], verbose_name='Имя')),
                ('age', models.IntegerField(blank=True, default=1, null=True, verbose_name='Возраст')),
                ('gender', models.BooleanField(blank=True, choices=[(None, 'Не определено'), (1, 'Мужской'), (0, 'Женский')], default=1, null=True, verbose_name='Пол')),
                ('address', models.CharField(blank=True, max_length=255, null=True, validators=[person.validators.validate_address_length], verbose_name='Адрес')),
                ('experience', models.IntegerField(validators=[person.validators.check_experience], verbose_name='Опыт работы')),
            ],
            options={
                'verbose_name': 'Человек',
                'verbose_name_plural': 'Люди',
                'ordering': ['pk'],
                'get_latest_by': ['-age'],
            },
        ),
        migrations.CreateModel(
            name='PersonsRelationShip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.child')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.person')),
            ],
            options={
                'verbose_name': 'Отношения',
                'verbose_name_plural': 'Отношения',
            },
        ),
        migrations.AddConstraint(
            model_name='person',
            constraint=models.CheckConstraint(check=models.Q(('age__gte', 16)), name='age'),
        ),
        migrations.AddField(
            model_name='child',
            name='parent_field',
            field=models.ManyToManyField(through='person.PersonsRelationShip', to='person.person'),
        ),
        migrations.AlterUniqueTogether(
            name='personsrelationship',
            unique_together={('child',)},
        ),
    ]
