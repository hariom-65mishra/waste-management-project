from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import WasteComplaint
from .forms import WasteComplaintForm, UserRegistrationForm

def home(request):
    total_count = WasteComplaint.objects.count()
    collected_count = WasteComplaint.objects.filter(status='Collected').count()
    in_progress_count = WasteComplaint.objects.filter(status='In Progress').count()
    pending_count = WasteComplaint.objects.filter(status='Pending').count()

    context = {
        'total_count': total_count,
        'collected_count': collected_count,
        'in_progress_count': in_progress_count,
        'pending_count': pending_count,
    }
    return render(request, 'home.html', context)

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome to CleanCity, {user.first_name or user.username}! Your account has been created.")
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

@login_required
def dashboard_view(request):
    user_complaints = WasteComplaint.objects.filter(user=request.user)
    recent_reports = user_complaints[:5]
    
    total = user_complaints.count()
    pending = user_complaints.filter(status='Pending').count()
    in_progress = user_complaints.filter(status='In Progress').count()
    collected = user_complaints.filter(status='Collected').count()

    context = {
        'recent_reports': recent_reports,
        'total': total,
        'pending': pending,
        'in_progress': in_progress,
        'collected': collected,
    }
    return render(request, 'dashboard.html', context)

@login_required
def report_waste_view(request):
    if request.method == 'POST':
        form = WasteComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            messages.success(request, f"Waste report {complaint.tracking_number} registered successfully! Our cleanup team has been notified.")
            return redirect('complaint_detail', pk=complaint.pk)
    else:
        form = WasteComplaintForm()

    return render(request, 'report_waste.html', {'form': form})

@login_required
def my_complaints_view(request):
    complaints = WasteComplaint.objects.filter(user=request.user)
    return render(request, 'my_reports.html', {'complaints': complaints})

@login_required
def complaint_detail_view(request, pk):
    complaint = get_object_or_404(WasteComplaint, pk=pk, user=request.user)
    return render(request, 'report_detail.html', {'complaint': complaint})
