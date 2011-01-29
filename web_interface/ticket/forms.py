from django.forms import ModelForm, ChoiceField, Select, widgets, Form
from ticket.models import Ticket, Answer

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ("query",)

class AnswerForm(ModelForm):    
    class Meta:
        model = Answer        
        fields = ("answer",)