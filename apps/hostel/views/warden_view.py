from django.shortcuts import render
from django.views.generic import ListView
from apps.hostel.forms import WardenSignUpForm,WardenSignUpTwo, WardenSearchForm,NoticeForm
from apps.hostel.models import User ,Warden,HostelStaff
from django.contrib.auth import login
from django.shortcuts import redirect
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from ..decorators import student_required, admin_required,hostelstaff_required,warden_required
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

@method_decorator([login_required], name='dispatch')
class WardenHomeView(ListView):
    template_name = 'warden_view/warden_home.html'

    def get(self,request):
        data=HostelStaff.objects.all()
        return render(request,self.template_name,{"data":data})

@login_required
@warden_required
def WardenSignUpView(request):
    if request.method == 'POST':
        main_form = WardenSignUpForm(request.POST)
        secondary_form = WardenSignUpTwo(request.user,request.POST)
        if main_form.is_valid() and secondary_form.is_valid():
            user = main_form.save()
            secondary_form.save(user)
            return redirect('admin_view:admin-home')
    else:
        main_form = WardenSignUpForm()
        secondary_form = WardenSignUpTwo(request.user)
    return render(request, 'admin_view/create_warden.html', {
        'main_form': main_form,
        'secondary_form': secondary_form
    })




class WardenUpdateView(BSModalUpdateView):
    model = Warden
    template_name = 'admin_view/update_warden.html'
    form_class = WardenSignUpTwo
    success_message = 'Success: Warden was updated.'
    success_url = reverse_lazy('admin_view:admin-home')

class WardenDeleteView(BSModalDeleteView):
    model = User
    context_object_name = 'field'
    template_name = 'admin_view/delete_warden.html'
    success_message = 'Success: Warden was deleted.'
    success_url = reverse_lazy('admin_view:admin-home')

class WardenReadView(BSModalReadView):
    model = Warden
    context_object_name = 'field'
    template_name = 'admin_view/read_warden.html'



def WardenSearchView(request):
    if request.method == 'POST':
        form=WardenSearchForm(request.POST)
        data=Warden.objects.filter(Q(firstName__icontains=form.data['search']) | Q(lastName__icontains=form.data['search']) | Q(hostel_name__icontains=form.data['search']))
        res=render(request,'admin_view/search_warden.html',{'form':form,'data':data})
        return res
    else:
        form=WardenSearchForm()
        res=render(request,'admin_view/search_warden.html',{'form':form})
        return res

def WardenCreateRequest(request):
    form = NoticeForm(request.user, request.POST or None)
    res=render(request,'warden_view/request.html',{'form':form})
    return res

def WardenAccount(request):
    res=render(request,'warden_view/create_notice.html')
    return res

def WardenCreateNotice(request):
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
    return render(request, 'warden_view/create_notice.html',context)
