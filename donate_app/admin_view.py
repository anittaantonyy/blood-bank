from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from donate_app.models import Donation, Complaint, Approve

@login_required(login_url='Login')
def admin_view_request(request):
    data = Donation.objects.all()
    return render(request, "admin_template/admin_view_request.html", {'new': data})
@login_required(login_url='Login')
def view_fulldonation_list(request):
    app_obj = Approve.objects.all()
    return render(request, "admin_template/total_donation.html", {'new': app_obj})
@login_required(login_url='Login')
def view_patient_complaint(request):
    complaint_data = Complaint.objects.all()
    return render(request, 'admin_template/view_patient_complaint.html', {'form': complaint_data})
@login_required(login_url='Login')
def update_patient_complaint(request,id):
    complaint_data = Complaint.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST.get("reply")
        complaint_data.reply = data
        complaint_data.save()
        return redirect("view_patient_complaint")
    return render(request,'admin_template/update_patient_complaint.html',{'form': complaint_data})
