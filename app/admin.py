from django.contrib import admin
from .models import *
# Register your models here.
class Writingmodeladmin(admin.ModelAdmin):
    readonly_fields = ('submit_time',)
    list_display = ['name', 'submit_time',]
admin.site.register(WritingModel, Writingmodeladmin)  
admin.site.register(newsletter)  
admin.site.register(Review)  