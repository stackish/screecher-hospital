from django.contrib import admin
from django.urls import path,include
from App import views

urlpatterns = [
    #path to render the admin 
    path('admin/', admin.site.urls),

    #path to render the homepage
    path('',views.frontend,name="frontend" ),

    # ====================
    #   LOGIN
    # ====================


    path('account/',include("django.contrib.auth.urls")),


    # ====================
    #   BACKEND
    # ====================
    #path to access the backend page
    path('backend/',views.backend,name="backend" ),

    #path to access the add page

    path('add_patient/',views.add_patient,name="add_patient" ),

    #path to delete patient

    path('delete_patient/<str:patient_id>/',views.delete_patient,name="delete_patient" ),

    #path to access the patients individually

    path('patient/<str:patient_id>/',views.patient,name="patient" ),

    #path to edit the patients


    path('edit_patient/<str:patient_id>/',views.edit_patient,name="edit_patient" ),






]
