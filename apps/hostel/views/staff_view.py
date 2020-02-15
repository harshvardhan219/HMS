from django.shortcuts import render
from django.views.generic import ListView
from apps.hostel.forms import StaffSignUpForm , StaffSignUpTwo,StaffSearchForm,NoticeForm
from apps.hostel.models import User ,HostelStaff,Student
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


# Create your views here.
class StaffHomeView(ListView):
    template_name = 'staff_view/staff_home.html'

    def get(self,request):
        data=Student.objects.all()
        return render(request,self.template_name,{"data":data})



def StaffSignUpView(request):
    if request.method == 'POST':
        main_form = StaffSignUpForm(request.POST)
        secondary_form = StaffSignUpTwo(request.user,request.POST)
        if main_form.is_valid() and secondary_form.is_valid():
            user = main_form.save()
            secondary_form.save(user)
            return redirect('warden_view:warden-home')
    else:
        main_form = StaffSignUpForm()
        secondary_form = StaffSignUpTwo(request.user)
    return render(request, 'warden_view/create_staff.html', {
        'main_form': main_form,
        'secondary_form': secondary_form
    })

class StaffUpdateView(BSModalUpdateView):
    model = HostelStaff
    template_name = 'warden_view/update_staff.html'
    form_class = StaffSignUpTwo
    success_message = 'Success: Staff was updated.'
    success_url = reverse_lazy('warden_view:warden-home')


class StaffReadView(BSModalReadView):
    model = HostelStaff
    context_object_name = 'field'
    template_name = 'warden_view/read_staff.html'


class StaffDeleteView(BSModalDeleteView):
    model = User
    context_object_name = 'field'
    template_name = 'warden_view/delete_staff.html'
    success_message = 'Success: Staff Member was deleted.'
    success_url = reverse_lazy('warden_view:warden-home')




def StaffSearchView(request):
    if request.method == 'POST':
        form=StaffSearchForm(request.POST)

        data=HostelStaff.objects.filter(Q(firstName__icontains=form.data['search']) | Q(lastName__icontains=form.data['search']) | Q(hostel_name__icontains=form.data['search']))
        res=render(request,'warden_view/search_staff.html',{'form':form,'data':data})
        return res

    else:
        form=StaffSearchForm()
        res=render(request,'warden_view/search_staff.html',{'form':form})
        return res


def StaffCreateNotice(request):
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
    return render(request, 'staff_view/create_notice.html',context)
