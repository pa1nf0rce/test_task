from uuid import uuid4

from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

CHOICES_BODY_TYPE = (
    ('Estate', 'Универсал'),
    ('Hatchback', 'Хэтчбек'),
    ('Pickup', 'Пикап'),
    ('Sedan', 'Седан'),
    ('Crossover Utility Vehicle (CUV)', 'Кроссовер'),
)

CHOICES_COLOR = (
    ('Gray', 'Серый'),
    ('Black', 'Чёрный'),
    ('White', 'Белый'),
    ('Blue', 'Синий'),
    ('Mixed', 'Смешанный'),
)

User = get_user_model()


class Car(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    brand = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    license_plate = models.CharField(
        max_length=6,
        validators=[RegexValidator(
               r'[АВЕКМНОРСТУХ]\d{3}(?!000)[АВЕКМНОРСТУХ]{2}'
            )]
        ,
        unique=True,
        help_text='Формат: X000XX или X000XX'
    )
    body_type = models.CharField(
        max_length=64,
        choices=CHOICES_BODY_TYPE
    )
    color = models.CharField(
        max_length=64,
        choices=CHOICES_COLOR
    )
    owner = models.ForeignKey(
        User,
        related_name='cars',
        on_delete=models.CASCADE,
    )

