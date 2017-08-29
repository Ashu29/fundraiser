from django.contrib import admin
from company import models
# Register your models here.
admin.site.register(models.Market)
admin.site.register(models.FundingDetail)


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    readonly_fields=('profile_id',)
