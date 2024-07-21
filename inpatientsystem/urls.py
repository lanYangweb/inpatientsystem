"""inpatientsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inpatientsystemApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('login/', views.login_page, name='login'),
    path('info/', views.info_page, name='info_page'),
    path('contact/', views.contact, name='contact_page'),

    path('admin/', admin.site.urls, name='admin'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_workspace/', views.admin_workspace, name='admin_workspace'),
    path('add_user/', views.add_user, name='add_user'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('doctor_login/', views.doctor_login, name='doctor_login'),
    path('doctor_workspace/', views.doctor_workspace, name='doctor_workspace'),
    # path('doctor_sign_up/', views.doctor_signup_view, name='doctor_sign_up_view'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('doctor_logout/', views.doctor_logout, name='doctor_logout'),

    # path('doctor_sign_up/doctor_login/', views.doctor_login, name='doctor_login'),
    path('doctor_workspace/add_patient/', views.add_patient, name='add_patient'),
    path('doctor_workspace/operating_room_booking/', views.operating_room_booking, name='operating_room_booking'),
    path('doctor_workspace/my_operation/', views.my_operation, name='my_operation'),
    # path('doctor_workspace/my_patient/', views.my_patient, name='my_patient'),
    path('doctor_workspace/add_operation/', views.add_operation, name='add_operation'),
    path('doctor_workspace/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('doctor_workspace/patients/', views.my_patients, name='patients'),
    path('discharge_patient/<int:patient_id>/', views.discharge_patient, name='discharge_patient'),
    path('doctor_workspace/my_booking_room/', views.my_booking_room, name='my_booking_room'),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    # path('check_overlapping_schedules/', views.check_overlapping_schedules, name='check_overlapping_schedules'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
