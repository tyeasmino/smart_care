from django.contrib import admin
from . import models 


class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}


# Register your models here.
admin.site.register(models.Doctor)
admin.site.register(models.Review)
admin.site.register(models.AvailableTime)
admin.site.register(models.Designation, DesignationAdmin)
admin.site.register(models.Specialization, SpecializationAdmin)


