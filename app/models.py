from __future__ import unicode_literals

from django.db import models


class MyModel(models.Model):
    my_field = models.CharField(max_length=255, db_index=True)
