from django.contrib.auth.forms import UserCreationForm
from django import forms

from donate_app.models import Login_view, Donor, Patient, Donation, Approve, Complaint, Patient_apply, Confirm


class LoginRegistration(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = Login_view
        fields = ('username','password1','password2')

class donor_form(forms.ModelForm):
    class Meta:
        model =Donor
        fields = ('__all__')
        exclude = ('user','status1')

class patient_form(forms.ModelForm):
    class Meta:
        model =Patient
        fields = ('__all__')
        exclude = ('user','status2')

class donation_form(forms.ModelForm):
    class Meta:
        model = Donation
        fields =('__all__')
        exclude = ('user', 'status3')

class patient_apply_form(forms.ModelForm):
    class Meta:
        model = Patient_apply
        fields = ('__all__')
        exclude = ('user','status4')

class approve_form(forms.ModelForm):
    class Meta:
        model = Approve
        fields =('__all__')
        exclude = ('user', 'approve_status5 ')


class confirm_form(forms.ModelForm):
    class Meta:
        model = Confirm
        fields = ('__all__')
        exclude = ('user',)



class complaint_form(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('complaint',)
