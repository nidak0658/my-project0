from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Job, Candidate, Application
from django.contrib import messages
from .forms import ResumeForm

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})

@login_required
def apply_for_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    candidate = request.user.candidate

    if request.method == 'POST':
        application = Application(job=job, candidate=candidate)
        application.save()
        messages.success(request, 'Application submitted successfully.')
        return redirect('job_list')

    return render(request, 'jobs/apply_for_job.html', {'job': job})

@login_required
def candidate_profile(request):
    candidate = request.user.candidate
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES, instance=candidate)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resume uploaded successfully.')
            return redirect('candidate_profile')
    else:
        form = ResumeForm(instance=candidate)
    
    return render(request, 'jobs/candidate_profile.html', {'form': form})

@login_required
def application_status(request):
    candidate = request.user.candidate
    applications = Application.objects.filter(candidate=candidate)
    return render(request, 'jobs/application_status.html', {'applications': applications})
