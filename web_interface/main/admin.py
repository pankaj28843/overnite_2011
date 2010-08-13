from main.models import *
from django.contrib import admin

class TestCaseInline(admin.TabularInline):
	model = TestCase
	extra = 1
class ProblemAdmin(admin.ModelAdmin):
    inlines = [TestCaseInline]
    search_fields = ['title', 'question']
    
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('problem','user', 'time','program','status','result','id')
    list_filter = ['time']
    search_fields = ['problem']
    date_hierarchy = 'time'
    
admin.site.register(Submission,SubmissionAdmin)
admin.site.register(Problem,ProblemAdmin)
