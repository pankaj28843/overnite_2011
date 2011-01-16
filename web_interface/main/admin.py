from main.models import *
from django.contrib import admin


def mark_public(modeladmin, request, queryset):
    queryset.update(is_public=True)
mark_public.short_description = "Mark selected stories as public"

def mark_not_public(modeladmin, request, queryset):
    queryset.update(is_public=False)
mark_not_public.short_description = "Mark selected stories as not public"

class TestCaseInline(admin.TabularInline):
	model = TestCase
	extra = 5
class ProblemAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/nicEdit.js','js/admin_wysiwg.js')
    list_display = ('title','is_public', 'no_of_test_cases', 'total_marks')
    inlines = [TestCaseInline]
    actions = [mark_public, mark_not_public]
    search_fields = ['title', 'question']
    
class SubmissionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,			   {'fields': ['problem']}),
		(None,			   {'fields': ['program']}),
		(None,			   {'fields': ['language']}),
	]
	list_display = ('problem','user', 'time','program','task_status','result','id','is_latest')
	list_filter = ['time']
	search_fields = ['problem']
	date_hierarchy = 'time'
	def save_model(self, request, obj, form, change): 
		instance = form.save(commit=False)
		instance.save(user = request.user)
		return instance
    
admin.site.register(Submission,SubmissionAdmin)
admin.site.register(Problem,ProblemAdmin)
