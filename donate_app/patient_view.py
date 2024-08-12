from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from donate_app.forms import approve_form, complaint_form, patient_apply_form
from donate_app.models import Donation, Patient, Approve, Complaint, Patient_apply

@login_required(login_url='Login')
def user_view_donation_list(request):
    data = Donation.objects.all()
    return render(request, "patient_template/user_view_donation_list.html", {'new': data})
@login_required(login_url='Login')
def patient_blood(request):
    if request.method == 'POST':
        u = request.user
        print(u)
        form = patient_apply_form(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            obj = form.save(commit=False)
            print(obj)
            obj.user = u
            obj.save()
            return redirect('view_patient_blood')
    else:
        form = patient_apply_form()
    return render(request, 'patient_template/view_patient_blood.html', {'form': form})
@login_required(login_url='Login')
def view_patient_blood(request):
    user = request.user
    data = Patient_apply.objects.filter(user=user)

    return render(request, "new_patient_blood.html", {'new': data})
@login_required(login_url='Login')
def delete_patient_blood_data(request,id):
    data = Patient_apply.objects.get(id=id)
    data.delete()
    return redirect("view_patient_blood")
@login_required(login_url='Login')
def update_patient_blood_data(request,id):
    data = Patient_apply.objects.get(id=id)
    form = patient_apply_form(instance=data)
    if request.method == 'POST':
        form = patient_apply_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("view_patient_blood")
    return render(request,'update_patient_blood_data.html',{'form': form})


@login_required(login_url='Login')
def complaint(request):
    if request.method == 'POST':
        user = request.user
        patient_data = Patient.objects.get(user=user)
        form = complaint_form(request.POST)
        if form.is_valid():
           obj = form.save(commit=False)
           print(obj)
           obj.user = patient_data
           obj.save()
           return redirect('view_complaint')
    else:
        form = complaint_form()
    return render(request, 'patient_template/complaint.html', {'form': form})
@login_required(login_url='Login')
def view_complaint(request):
    user = request.user
    patient_data = Patient.objects.get(user=user)
    complaint_data = Complaint.objects.filter(user=patient_data)
    return render(request, 'patient_template/view_complaint.html', {'form': complaint_data})


