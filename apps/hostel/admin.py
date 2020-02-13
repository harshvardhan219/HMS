from django.contrib import admin

# Register your models here.
from apps.hostel import models

admin.site.register(models.User)
admin.site.register(models.Warden)
admin.site.register(models.HostelStaff)
admin.site.register(models.Student)
admin.site.register(models.Parent)
'''
from django.paths import path,include
from django.contrib.auth import views as auth_view
from .views import dashboard,admin_view,warden_view,staff_view,student_view,parent_view

urlpatterns = [
    path('admin/', include(([
        path('admin-home',admin_view.AdminHomeView.as_view(),name='admin-home'),
        path('Notice-admin/',admin_view.AdminCreateNotice,name='create-notice'),

    ], 'dashboard'),namespace='admin_view')),

    path('warden/', include(([
        path('warden-home/',warden_view.WardenHomeView.as_view(),name='warden-home'),
        path('signupWarden/',warden_view.WardenSignUpView,name='signupWarden'),
        path('search-warden/',warden_view.WardenSearchView,name='search-warden'),
        path('notice-warden/',warden_view.WardenCreateNotice,name='create-notice'),

    ], 'dashboard'),namespace='warden_view')),

    path('staff/', include(([
        path('signupStaff/',staff_view.StaffSignUpView,name='signupstaff'),
        path('search-staff/',staff_view.StaffSearchView,name='search-staff'),
        path('staff-home/',staff_view.StaffHomeView.as_view(),name='warden-home'),
        path('notice-staff/',staff_view.StaffCreateNotice,name='create-notice'),


    ], 'dashboard'),namespace='staff_view')),

    path('student/', include(([

    ], 'dashboard'),namespace='student_view')),

#    path('update/<int:pk>', WardenUpdateView.as_view(), name='update_warden'),
#    path('read/<int:pk>', WardenReadView.as_view(), name='read_warden'),
#    path('delete/<int:pk>',WardenDeleteView.as_view(), name='delete_warden'),

]
'''
