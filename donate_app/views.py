from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from donate_app.forms import LoginRegistration, donor_form, patient_form
from donate_app.models import Patient, Donor


# Create your views here.
def index(request):
    return render(request, "app.html")

def about(request):
    return render(request, "new.html")
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        print(username)
        password = request.POST.get('pass')
        print(password)
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin_template')
            elif user.is_donor:
                return redirect('donor_template')
            elif user.is_patient:
                return redirect('patient_template')
            # else:
            #     messages.info(request,'InvalidCredentials')
    return render(request, "login.html")

@login_required(login_url='Login')
def admin_template(request):
    return render(request, "admin_template/admin_template.html")

@login_required(login_url='Login')
def donor_template(request):
    return render(request, "donor_template/donor_template.html")
@login_required(login_url='Login')
def patient_template(request):
    return render(request, "patient_template/patient_template.html")

def donor_add(request):
    form1 = LoginRegistration()
    form2 = donor_form()
    if request.method == 'POST':
        form1 = LoginRegistration(request.POST)
        form2 = donor_form(request.POST)

        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_donor = True
            a.save()
            user1 = form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect('Login')
    return render(request, 'registration.html', {'form1': form1, 'form2': form2})

def patient_add(request):
    form1 = LoginRegistration()
    form2 = patient_form()
    if request.method == 'POST':
        form1 = LoginRegistration(request.POST)
        form2 = patient_form(request.POST)

        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_patient = True
            a.save()
            user1 = form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect('Login')
    return render(request, 'patient_registration.html', {'form1': form1, 'form2': form2})

@login_required(login_url='Login')
def view_patient(request):
    data = Patient.objects.all()
    return render(request, "new_patient.html", {'new': data})
@login_required(login_url='Login')
def delete_patient_data(request,id):
    data = Patient.objects.get(id=id)
    data.delete()
    return redirect("view_patient")
@login_required(login_url='Login')
def update_patient_data(request,id):
    data = Patient.objects.get(id=id)
    form = patient_form(instance=data)
    if request.method == 'POST':
        form = patient_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("view_patient")
    return render(request,'update_patient_data.html',{'form':form})
@login_required(login_url='Login')
def view_donor(request):
    data = Donor.objects.all()
    return render(request, "new_donor.html", {'new': data})
@login_required(login_url='Login')
def delete_donor_data(request,id):
    data = Donor.objects.get(id=id)
    data.delete()
    return redirect("view_donor")
@login_required(login_url='Login')
def update_donor_data(request,id):
    data = Donor.objects.get(id=id)
    form = donor_form(instance=data)
    if request.method == 'POST':
        form = donor_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("view_donor")
    return render(request,'update_donor_data.html',{'form': form})

def Logout(request):
    return redirect("Login")

