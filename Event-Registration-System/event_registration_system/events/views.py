from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, Registration
from django.utils import timezone

def event_list(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    user = request.user

    # Check if the user is already registered
    existing_registration = Registration.objects.filter(user=user, event=event).exists()

    if existing_registration:
        message = f"You are already registered for {event.title}."
    else:
        registration = Registration(user=user, event=event)
        registration.save()
        message = f"Successfully registered for {event.title}."

    return render(request, 'events/registration_status.html', {'message': message})

@login_required
def user_registrations(request):
    user = request.user
    registrations = Registration.objects.filter(user=user).order_by('-registration_date')
    return render(request, 'events/user_registrations.html', {'registrations': registrations})
