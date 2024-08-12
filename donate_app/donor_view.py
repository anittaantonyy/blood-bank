from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from donate_app.forms import donation_form, confirm_form
from donate_app.models import Donation, Donor, Approve, Patient_apply
@login_required(login_url='Login')
def donor_view_donation_list(request):
    data = Patient_apply.objects.all()
    return render(request, "donor_template/donor_view_donation_list.html", {'new': data})
@login_required(login_url='Login')
def add_to_approve(request,id):
    data = Patient_apply.objects.get(id=id)
    user = request.user
    user_data = Donor.objects.get(user=user)
    print(user_data)
    obj = Approve(user=user_data, product=data)
    obj.save()
    return redirect("view_approve")

@login_required(login_url='Login')
def view_approve(request):
    user = request.user
    data = Donor.objects.get(user=user)
    app_obj = Approve.objects.filter(user=data)
    return render(request, "donor_template/view_approve.html", {'new': app_obj })
@login_required(login_url='Login')
def approve_patient(request,id):
    data = Approve.objects.get(id=id)
    con_form = confirm_form()
    if request.method == 'POST':
        form = confirm_form(request.POST)
        print(form)
        if form.is_valid():
            data.approve_status5 = 1
            data.save()
            obj = form.save(commit=False)
            obj.user = data
            print(obj)
            obj.save()
            return redirect('view_approve')
    return render(request, "donor_template/approve.html", {'form': con_form})
@login_required(login_url='Login')
def approved_patient(request):
    user = request.user
    data = Donor.objects.get(user=user)
    app_obj = Approve.objects.filter(user=data, approve_status5=1)
    return render(request, "donor_template/approved_patient.html", {'new': app_obj })


@login_required(login_url='Login')
def donor_blood(request):
    if request.method == 'POST':
        u = request.user
        print(u)
        form = donation_form(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            obj = form.save(commit=False)
            print(obj)
            obj.user = u
            obj.save()
            return redirect('view_donor_blood')
    else:
        form = donation_form()
    return render(request, 'donor_template/view_donor_blood.html', {'form': form})
@login_required(login_url='Login')
def view_donor_blood(request):
    user = request.user
    data = Donation.objects.filter(user=user)

    return render(request, "new_donor_blood.html", {'new': data})
@login_required(login_url='Login')
def delete_donor_blood_data(request,id):
    data = Donation.objects.get(id=id)
    data.delete()
    return redirect("view_donor_blood")
@login_required(login_url='Login')
def update_donor_blood_data(request,id):
    data = Donation.objects.get(id=id)
    form = donation_form(instance=data)
    if request.method == 'POST':
        form = donation_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("view_donor_blood")
    return render(request,'update_donor_blood_data.html',{'form': form})

