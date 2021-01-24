from django.db import models
from django.urls import reverse

class volinteer(models.Model):
    firstname = models.CharField(max_length=200, help_text='Enter your first name (e.g. Jhon)')
    lastname = models.CharField(max_length=200, help_text='Enter your last name (e.g. Jhon)')
    username = models.CharField(max_length=200, help_text='Enter your username (e.g. Jhon123)')

    EARLY_ADRESS_CHOICES = (
        ('10', 'The moon'),
        ('11', '323 East West st, Hilsborough, 27278'),
        ('12', '576 North South st, Hillsborough, 27278'),
        ('13', '1536 King st, Hillsborough, 27278'),
        ('14', '12021 President st, Hillsborough, 27278'),
        ('21', '321 Book st, Durham, 27517'),
        ('22', '456 Novel st, Durham, 27517'),
        ('23', '613 Film st, Durham, 27517'),
        ('24', '11 TV st, Durham, 27517'),
    )
    

    adress = models.CharField(
        max_length=2,
        choices=EARLY_ADRESS_CHOICES,
        blank=True,
        default='10',
        help_text='Your adress',
        )

    def __str__(self):
        return self.username

# Create your models here.
