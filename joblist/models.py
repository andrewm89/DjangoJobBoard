from __future__ import unicode_literals

from django.db import models

# Create your models here.
class availablejobs(models.Model):
    jobtitle = models.CharField(max_length=200, null=False)
    postdate = models.DateField(auto_now_add=True)
    jobdescription = models.TextField(max_length=500, null=False)