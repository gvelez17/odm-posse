from django.contrib import admin

# Register your models here.

from .models import Ad, Org, Donor

admin.site.register(Ad)
admin.site.register(Org)
admin.site.register(Donor)
