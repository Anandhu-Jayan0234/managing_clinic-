from django.contrib import admin
from django.urls import path, include
from .views import About,Home, Contact, Login, Index, Logout_admin, View_doctor, Delete_doctor, Add_doctor,View_patient,Add_appointment , View_appointment, Delete_appointment ,Delete_patient, Add_patient
urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('admin_login/', Login, name='admin_login'),
    path('logout/', Logout_admin, name='logout_admin'),
    path('index/', Index, name='dashboard'),
    path('view_doctor/', View_doctor, name='view_doctor'),
    path('add_doctor/',Add_doctor, name='add_doctor'),
    path('delete_doctor(?P<int:pid>)/', Delete_doctor, name='delete_doctor'),
    path('view_patient/', View_patient, name='view_patient'),
    path('add_patient/', Add_patient, name='add_patient'),
    path('delete_patient(?P<int:pid>)/', Delete_patient, name='delete_patient'),
    path('view_appointment/', View_appointment, name='view_appointment'),
    path('delete_appointment(?P<int:pid>)/', Delete_appointment, name='delete_appointment'),
    path('add_appointment/', Add_appointment, name='add_appointment'),
]

