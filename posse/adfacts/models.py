from django.db import models

# Create your models here.

class Donor(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    full_name = models.CharField(max_length=256)
    email = models.CharField(max_length=128)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=15)
    country = models.CharField(max_length=32)
    notes = models.TextField()
       
class Org(models.Model):
    name = models.CharField(max_length=256)
    sos_link = models.CharField(max_length=256)
    notes = models.TextField()
    donors = models.ManyToManyField(Donor)

class Ad(models.Model):
    title = models.CharField(max_length=256)
    desc = models.TextField()
    paid_by = models.ForeignKey(Org, on_delete=models.PROTECT)
    in_support_of = models.CharField(max_length=256)
    opposing = models.CharField(max_length=256)
    first_seen = models.DateTimeField(blank=True, null=True)
    last_seen = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

