from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('hostel', include('apps.hostel.urls')),

]
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_view
#admin_view
from apps.hostel.views.admin_view import AdminHomeView, WardenSignUpView,WardenSearchView,AdminCreateNotice,WardenLoginView
# warden_view
from apps.hostel.views.warden_view import WardenHomeView,StaffSignUpView,WardenCreateNotice,StaffSearchView,WardenPayView
#staff_view
from apps.hostel.views.staff_view import StaffHomeView,StudentSignUpView,StaffCreateNotice,StudentSearchView,StaffPayView

urlpatterns = [
    #admin urls
    path('admin/', admin.site.urls),
    url('admin-home',AdminHomeView.as_view(),name='admin-home'),
    url('signupWarden/',WardenSignUpView,name='signupWarden'),
    url('search-warden/',WardenSearchView,name='search-warden'),
    url('Notice-admin/',AdminCreateNotice,name='create-notice'),
    #Warden urls
    url('warden-home/',WardenHomeView.as_view(),name='warden-home'),
    url('signupStaff/',StaffSignUpView,name='signupstaff'),
    url('notice-warden/',WardenCreateNotice,name='create-notice'),
    url('search-staff/',StaffSearchView,name='search-staff'),
    url('warden-payment/',WardenPayView,name='payment-staff'),
    #staff URLs
    url('staff-home/',StaffHomeView.as_view(),name='warden-home'),
    url('signupStudent/',StudentSignUpView,name='signupstudent'),
    url('notice-staff/',StaffCreateNotice,name='create-notice'),
    url('search-student/',StudentSearchView,name='search-staff'),
    url('staff-payment/',StaffPayView,name='payment-staff'),

]
