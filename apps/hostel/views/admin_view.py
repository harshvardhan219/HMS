from django.shortcuts import render
from django.views.generic import ListView
from apps.hostel.forms import WardenSignUpForm,WardenSignUpTwo, WardenSearchForm
from apps.hostel.models import User ,Warden
from django.contrib.auth import login
from django.shortcuts import redirect
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

class AdminSignUpView(ListView):
    pass

class AdminHomeView(generic.ListView):
    model = Warden
    context_object_name = 'data'
    template_name = 'admin_view/admin_home.html'

def AdminCreateNotice(request):
    res=render(request,'admin_view/create_notice.html')
    return res
