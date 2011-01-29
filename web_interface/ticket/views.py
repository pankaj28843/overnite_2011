from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from ticket.models import Ticket, Answer
from ticket.forms import TicketForm, AnswerForm

@login_required
def submit_ticket(request):
    if request.method == 'POST': # If the form has been submitted...
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket_obj = form.save(commit=False)
            ticket_obj.user = request.user
            ticket_obj.save()
            return HttpResponseRedirect("/ticket/%d/"%(ticket_obj.id))
    else:
        form = TicketForm()
        context = RequestContext(request)
        return render_to_response("ticket/submit_ticket.html", {"form":form}, context_instance = context)

@login_required
def list_tickets(request):
    if request.user:
        if request.user.is_superuser:
            tickets = Ticket.objects.all()
        else:
            tickets = Ticket.objects.filter(user=request.user)
    tickets = tickets.order_by('-time')
    context = RequestContext(request)
    return render_to_response("ticket/list_tickets.html", {"tickets":tickets}, context_instance = context)

@login_required
def show_ticket(request, id):
    if request.user.is_superuser:
        ticket = get_object_or_404(Ticket, pk=id)
    else:
        ticket = get_object_or_404(Ticket, pk=id, user=request.user)
    answers = Answer.objects.all().filter(ticket = ticket)
    
    if request.method == 'POST': # If the form has been submitted...
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer_obj = form.save(commit=False)
            answer_obj.user = request.user
            answer_obj.ticket = ticket
            answer_obj.save()
            form = AnswerForm()
    else:
        form = AnswerForm()
        
    context = RequestContext(request)
    return render_to_response("ticket/show_ticket.html", {"ticket":ticket,"answers":answers, "form":form,}, context_instance = context)

@login_required
def mark_solved(request, id):
    ticket = get_object_or_404(Ticket, pk=id, user=request.user)
    ticket.solved = True
    ticket.save()
    return HttpResponseRedirect("/ticket/")
