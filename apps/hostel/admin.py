from django.contrib import admin

# Register your models here.
from apps.hostel import models

admin.site.register(models.User)
admin.site.register(models.Warden)
admin.site.register(models.HostelStaff)
admin.site.register(models.Student)
admin.site.register(models.Parent)
