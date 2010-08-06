from main.models import *
from django.contrib import admin

class InputOutPutInline(admin.TabularInline):
	model = InputOutput
	extra = 1
class ProblemAdmin(admin.ModelAdmin):
    inlines = [InputOutPutInline]
    list_display = ('title','id')
    search_fields = ['title', 'question']
    
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('problem','program','status','result','id')
    list_filter = ['time']
    search_fields = ['problem']
    date_hierarchy = 'time'
    
admin.site.register(Submission,SubmissionAdmin)
admin.site.register(Problem,ProblemAdmin)
