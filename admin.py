from django.contrib import admin
from PR import models

# Register your models here.
admin.site.register(models.applicant_info)
# admin.site.register(models.additional_info)
# admin.site.register(models.passport_info)
admin.site.register(models.martial_status)
admin.site.register(models.children_info)
admin.site.register(models.family_info)
# admin.site.register(models.education_details)
admin.site.register(models.fee_structure)
# admin.site.register(models.job_detail)
admin.site.register(models.address_details)
admin.site.register(models.travel_history)
admin.site.register(models.background_in_canada)
admin.site.register(models.documents)


