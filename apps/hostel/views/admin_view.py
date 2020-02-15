from django.shortcuts import render
from django.views.generic import ListView
from apps.hostel.forms import WardenSignUpForm,WardenSignUpTwo, WardenSearchForm,NoticeForm
from apps.hostel.models import User ,Warden,Admin
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
    form = NoticeForm(request.user, request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print('Saved notice')
            form.save(request.user)
            form = NoticeForm(request.user)
    context = {
        'form': form,
        'user': request.user,
    }
    return render(request, 'admin_view/create_notice.html',context)

class AdminProfileView(BSModalReadView):
       model = Admin
       context_object_name = 'field'
       template_name = 'admin_view/read_warden.html'
