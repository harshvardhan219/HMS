from django.urls import path,include
from django.contrib.auth import views as auth_view
from .views import dashboard,admin_view,warden_view,staff_view,student_view,parent_view

urlpatterns = [
    path('admin/', include(([
        path('admin-home',admin_view.AdminHomeView.as_view(),name='admin-home'),
        path('notice-admin/',admin_view.AdminCreateNotice,name='notice-admin'),

    ], 'dashboard'),namespace='admin_view')),

    path('warden/', include(([
        path('warden-home/',warden_view.WardenHomeView.as_view(),name='warden-home'),
        path('signupWarden/',warden_view.WardenSignUpView,name='signupWarden'),
        path('search-warden/',warden_view.WardenSearchView,name='search-warden'),
        path('notice-warden/',warden_view.WardenCreateNotice,name='notice-warden'),
        path('request-warden/',warden_view.WardenCreateNotice,name='request-warden'),
        path('account-warden/',warden_view.WardenCreateNotice,name='account-warden'),
        path('update/<int:pk>',warden_view.WardenUpdateView.as_view(), name='update_warden'),
        path('read/<int:pk>', warden_view.WardenReadView.as_view(), name='read_warden'),
        path('delete/<int:pk>',warden_view.WardenDeleteView.as_view(), name='delete_warden'),

    ], 'dashboard'),namespace='warden_view')),

    path('staff/', include(([
        path('signupStaff/',staff_view.StaffSignUpView,name='signupStaff'),
        path('search-staff/',staff_view.StaffSearchView,name='search-staff'),
        path('staff-home/',staff_view.StaffHomeView.as_view(),name='warden-home'),
        path('notice-staff/',staff_view.StaffCreateNotice,name='notice-staff'),
        path('staff-request/',staff_view.StaffCreateNotice,name='staff-request'),
        path('staff-account/',warden_view.WardenCreateNotice,name='staff-account'),
        path('update/<int:pk>',staff_view.StaffUpdateView.as_view(), name='update_staff'),
        path('read/<int:pk>', staff_view.StaffReadView.as_view(), name='read_staff'),
        path('delete/<int:pk>',staff_view.StaffDeleteView.as_view(), name='delete_staff'),


    ], 'dashboard'),namespace='staff_view')),

    path('student/', include(([
        path('signupStudent/',student_view.StudentSignUpView,name='signupStudent'),
        path('search-student/',student_view.StudentSearchView,name='search-student'),
    ], 'dashboard'),namespace='student_view')),


]
