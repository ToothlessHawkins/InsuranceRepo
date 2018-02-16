# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    corporation = models.CharField(max_length=50)
    billing_address = models.CharField(max_length=50)
    phone_number = models.BigIntegerField()
    email_address = models.EmailField()
    user_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return "{}".format(self.user_name)

class driver(models.Model):
    first_name = models.ForeignKey(account, related_name="firstname", on_delete=models.SET_NULL, null=True)
    last_name = models.ForeignKey(account, related_name="lastname", on_delete=models.SET_NULL, null=True)
    user_name = models.ForeignKey(account, related_name="username", on_delete=models.SET_NULL, null=True)
    suffix = models.CharField(max_length=50)
    license_plate_num = models.CharField(max_length=7)
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('n', 'prefer not to answer'),
         )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='n')
    DRIVER_CHOICES = (
        ('LP', 'Learners Permits'),
        ('DL', 'Drivers License'),
        ('R', 'Revoked'),
        ('S', 'Suspended'),
    )
    active_driver = models.CharField(max_length=2, choices=DRIVER_CHOICES)
    driver_state_of_residence = models.CharField(max_length=50)
    num_of_collisions = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.user_name)

class vehicle(models.Model):
    user_name = models.ForeignKey(account, related_name="Username", on_delete=models.SET_NULL, null=True)
    MODEL_OPTIONS = (
        ('T', 'Toyota'),
        ('N', 'Nissan'),
        ('F', 'Ford'),
        ('VB', 'Volkswagon Beetle'),
        ('J', 'Jeep'),
        ('C', 'Chrysler'),
        ('CH', 'Chevrolet'),
        ('AU', 'Audi'),
        ('AM', 'Aston Martin'),
        ('AC', 'Acura'),
        ('B', 'BMW'),
        ('CD', 'Cadillac'),
        ('CR', 'Corvette'),
        ('D', 'Dodge'),
        ('G', 'GMC'),
        ('HN', 'Honda'),
        ('HY', 'Hyundai'),
        ('HM', 'Hummer'),
        ('IS', 'Isuzu'),
        ('IN', 'Infiniti'),
        ('JG', 'Jaguar'),
        ('LM', 'Lamborghini'),
        ('LR', 'Landrover'),
        ('LN', 'Lincoln'),
    )
    car_model = models.CharField(max_length=50, choices=MODEL_OPTIONS)
    CENTURY = (
        ('20th Century', '1900-1999'),
        ('21th Century', '2000-2099'),
    )
    year_of_purchase = models.CharField(max_length=12, choices=CENTURY)
    COLOR_OPTIONS = (
        ('R', 'Red'),
        ('BL', 'Blue'),
        ('G', 'Green'),
        ('WH', 'White'),
        ('G', 'Grey'),
        ('BLK', 'Black'),
        ('P', 'Pink'),
        ('PR', 'Purple'),
        ('Y', 'Yellow'),
    )
    car_color = models.CharField(max_length=10, choices=COLOR_OPTIONS)
    CONDITION_OPTIONS = (
        ('G', 'Good Condition'),
        ('NG', 'Not So Good Condition'),
        ('B', 'Bad Condition'),
        ('T', 'Totaled'),
    )
    car_condition = models.CharField(max_length=50, choices=CONDITION_OPTIONS)
    car_condition_details = models.TextField(max_length=100, blank=True, null=True)
    RANGE_OPTIONS = (
        ('LOW', '0-10000'),
        ('NORMAL', '10000-50000'),
        ('HIGH', '50000-100000'),
    )
    car_mileage = models.CharField(max_length=20, choices=RANGE_OPTIONS)
    vehicle_num = models.CharField(max_length=17, primary_key=True, unique=True)
    purchase_date = models.DateField()
    YEAR_RANGE = (
        ('LOW', '0-100'),
        ('NORMAL', '100-200'),
        ('HIGH', '200-300'),
    )
    miles_per_year = models.CharField(max_length=10, choices=YEAR_RANGE)

    def __str__(self):
        return "{}".format(self.car_model)