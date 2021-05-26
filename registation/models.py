from django.db import models


class UserTrack(models.Model):
    gender_type = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    fname = models.CharField(max_length=50, verbose_name='First Name')
    lname = models.CharField(max_length=50, verbose_name='Last Name')
    birthday = models.DateField(verbose_name='Date of Birth')
    gender = models.CharField(max_length=10, choices=gender_type, default=gender_type[0][0], verbose_name='Gender')
    email = models.EmailField(max_length=1000, verbose_name='Email Address')
    phone_number = models.CharField(max_length=15, verbose_name='Phone Number')
    nid = models.CharField(max_length=30, blank=True, null=True, verbose_name='NID Number')

    def __str__(self):
        return self.fname + self.lname
from django.db import models

# Create your models here.
