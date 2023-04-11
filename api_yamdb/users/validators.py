import re

from django.core.exceptions import ValidationError


def username_validation(value):
    if value.lower() == "me":
        raise ValidationError(
            "Вы не можете использовать 'me' в качестве username"
        )
    if not re.match(r'[\w.@+-]+\Z', value):
        raise ValidationError(
            'В имени пользователя недопустимые символы'
        )
