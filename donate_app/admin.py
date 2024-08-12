from django.contrib import admin

from donate_app import models

# Register your models here.
admin.site.register(models.Login_view)
admin.site.register(models.Patient)
admin.site.register(models.Donor)
admin.site.register(models.Donation)
admin.site.register(models.Patient_apply)
admin.site.register(models.Approve)
admin.site.register(models.Confirm)

