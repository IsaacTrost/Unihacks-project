from django.db import models
from django.urls import reverse

class volinteer(models.Model):
    firstname = models.CharField(max_length=200, help_text='Enter your first name (e.g. Jhon)')
    lastname = models.CharField(max_length=200, help_text='Enter your last name (e.g. Jhon)')
    username = models.CharField(max_length=200, help_text='Enter your username (e.g. Jhon)')

        LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )
    def __str__(self):
        return self.username

# Create your models here.
