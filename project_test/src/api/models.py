from django.db import models


class Tests(models.Model):
    login = models.CharField(
        max_length=10,
        unique=True,
    )
    iq_time = models.DateTimeField(
        null=True,
    )
    iq_score = models.IntegerField(
        null=True,
    )
    eq_letters = models.CharField(
        max_length=5,
        null=True,
    )
    eq_time = models.DateTimeField(
        null=True,
    )
