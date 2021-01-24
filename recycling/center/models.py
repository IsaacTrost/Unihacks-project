from django.db import models

class wastecenter(models.Model):
    name = models.CharField(max_length=200, help_text='Enter the name of the center')
    adress = models.CharField(max_length=200, help_text='Enter the adress of the center')
    summery = models.CharField(max_length=200, help_text='A brief discription')
    picture = models.ImageField()

    ACCEPTED_ITEMS = (
        ('1', 'batteries'),
        ('2', 'oil'),
        ('3', 'acids'),
        ('4', 'all three'),

    )

    adress = models.CharField(
        max_length=1,
        choices=ACCEPTED_ITEMS,
        blank=True,
        default='4',
            )

    def __str__(self):
        return self.name

class pickuppoints(models.Model):
    adress = models.CharField(max_length=200, help_text='Enter the adress of the pickup point')
    discription = models.CharField(max_length=200, help_text='Enter a discription of the point')

    STREET = (
        ('1', 'East'),
        ('2', 'West'),
        ('3', 'King'),
        ('4', 'Queen'),
    )
    NEIGHBORHOOD = (
        ('1', 'Hillsborough'),
        ('2', 'Durham'),
    )

    city = models.CharField(
        max_length=1,
        choices=NEIGHBORHOOD,
        blank=True,
        default='1',
        )
    street = models.CharField(
        max_length=1,
        choices=STREET,
        blank=True,
        default='1',
        )


# Create your models here.
