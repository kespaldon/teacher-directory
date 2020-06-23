from django.contrib.postgres.fields.array import ArrayField
from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_picture = models.CharField(max_length=64)
    email_address = models.EmailField(unique=True, max_length=254)
    phone_number = models.CharField(max_length=15)
    room_number = models.CharField(max_length=16)
    subjects_taught = models.CharField(max_length=512, default="")
