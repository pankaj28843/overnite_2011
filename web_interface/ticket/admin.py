from django.contrib import admin
from ticket.models import Ticket, Answer

class AnswerInlineAdmin(admin.TabularInline):
    model = Answer
    extra = 1
    
class TicketAdmin(admin.ModelAdmin):
    inlines = [AnswerInlineAdmin]
    

admin.site.register(Ticket, TicketAdmin)