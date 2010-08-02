from main.models import *
from django.contrib import admin
    
class SubmissionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['program']}),
        (None,               {'fields': ['input_file']}),
        (None,               {'fields': ['output_file']}),
    ]
    list_display = ('name','program','id')
    list_filter = ['time']
    search_fields = ['name']
    date_hierarchy = 'time'
    
admin.site.register(Submission,SubmissionAdmin)
