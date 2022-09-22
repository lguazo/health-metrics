from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30, help_text='30 caracteres max.')
    lastname = models.CharField(max_length=30, help_text='30 caracteres max.')
    age = models.IntegerField()
    weight = models.IntegerField()
    heartRate = models.IntegerField(help_text="Heart rate measured in Beats per minute/Pulses per minute")
    SpO2 = models.IntegerField(help_text="Blood Oxygen Saturation")

    STRESS_LEVEL = (
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
        ('extreme', 'Extreme'),
    )

    stresslevel = models.CharField(max_length=25, choices=STRESS_LEVEL, default='low')
