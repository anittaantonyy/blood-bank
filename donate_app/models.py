from django.contrib.auth.models import AbstractUser
from django.db import models


class Login_view(AbstractUser):
    is_donor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

class Donor(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE, related_name='donor')
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    blood_type = models.CharField(max_length=30)
    status1 = models.BooleanField(default=0)

class Patient(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE, related_name='patient')
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    blood_type = models.CharField(max_length=30)
    status2 = models.BooleanField(default=0)


class Donation(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE, related_name='donation')
    name = models.CharField(max_length=50)
    quantity =models.CharField(max_length=10)
    location = models.CharField(max_length=255)
    status3 = models.BooleanField(default=0)

class Patient_apply(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE, related_name='patient_apply')
    name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=10)
    location = models.CharField(max_length=255)
    status4 = models.BooleanField(default=0)

class Approve(models.Model):
    user = models.ForeignKey(Donor, on_delete=models.CASCADE, related_name='add_donation')
    product = models.ForeignKey(Patient_apply, on_delete=models.CASCADE, related_name='add_donation')
    approve_status5 = models.IntegerField(default=0)


class Confirm(models.Model):
    user = models.ForeignKey(Approve, on_delete=models.CASCADE, related_name='confirm_now')
    patient_number = models.CharField(max_length=16)


class Complaint(models.Model):
    user = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='complaint')
    date = models.DateField(auto_now_add=True)
    complaint = models.CharField(max_length=100)
    reply = models.CharField(max_length=150,null=True,blank=True)