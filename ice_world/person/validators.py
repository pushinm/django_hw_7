from django.core.exceptions import ValidationError
import re

def validate_address_length(value):
    pattern = r'^[а-яА-Яa-zA-z0-9\ \.\,\-]*'
    if re.match(pattern, value).span()[1] != len(value):
        raise ValidationError('Строка не должна содержать специальные символы')

def check_experience(value):
    if int(value) <= 3:
        raise ValidationError('Не принимаем на работу кадров без опыта работы меньше 3-х лет')