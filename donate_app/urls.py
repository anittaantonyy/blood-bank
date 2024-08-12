from django.contrib import admin
from django.urls import path, include

from donate_app import views, donor_view, patient_view, admin_view

urlpatterns = [
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("Login",views.Login,name="Login"),
    path("admin_template",views.admin_template,name="admin_template"),
    path("donor_template",views.donor_template,name="donor_template"),
    path("patient_template",views.patient_template,name="patient_template"),
    path("donor_add",views.donor_add,name="donor_add"),
    path("patient_add",views.patient_add,name="patient_add"),
    path("view_patient", views.view_patient, name="view_patient"),
    path("delete_patient_data/<int:id>/", views.delete_patient_data, name="delete_patient_data"),
    path("update_patient_data/<int:id>/", views.update_patient_data, name="update_patient_data"),
    path("view_donor", views.view_donor, name="view_donor"),
    path("delete_donor_data/<int:id>/", views.delete_donor_data, name="delete_donor_data"),
    path("update_donor_data/<int:id>/", views.update_donor_data, name="update_donor_data"),
    path("donor_view",donor_view.donor_view_donation_list, name="donor_view_donation_list"),
    path("donor_blood", donor_view.donor_blood, name="donor_blood"),
    path("view_donor_blood", donor_view.view_donor_blood, name="view_donor_blood"),
    path("delete_donor_blood_data/<int:id>/", donor_view.delete_donor_blood_data, name="delete_donor_blood_data"),
    path("update_donor_blood_data/<int:id>/", donor_view.update_donor_blood_data, name="update_donor_blood_data"),
    path("add_to_approve/<int:id>/", donor_view.add_to_approve, name="add_to_approve"),
    path("view_approve",donor_view.view_approve, name="view_approve"),
    path("approve_patient/<int:id>/", donor_view.approve_patient, name="approve_patient"),
    path("approved_patient", donor_view.approved_patient, name="approved_patient"),


    path("patient_view", patient_view.user_view_donation_list, name="user_view_donation_list"),
    path("patient_blood", patient_view.patient_blood, name="patient_blood"),
    path("view_patient_blood", patient_view.view_patient_blood, name="view_patient_blood"),
    path("delete_patient_blood_data/<int:id>/", patient_view.delete_patient_blood_data, name="delete_patient_blood_data"),
    path("update_patient_blood_data/<int:id>/", patient_view.update_patient_blood_data, name="update_patient_blood_data"),



    path("admin_view", admin_view.admin_view_request, name="admin_view_request"),
    path("view_fulldonation_list", admin_view.view_fulldonation_list, name="view_fulldonation_list"),
    path("complaint", patient_view.complaint, name="complaint"),
    path("view_complaint", patient_view.view_complaint, name="view_complaint"),
    path("view_patient_complaint", admin_view.view_patient_complaint, name="view_patient_complaint"),
    path("update_patient_complaint/<int:id>/", admin_view.update_patient_complaint, name="update_patient_complaint"),
    path("Logout",views.Logout,name="Logout")
]