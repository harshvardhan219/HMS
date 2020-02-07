from django.shortcuts import render
from django.views.generic import ListView
from apps.hostel.forms import StaffSignUpForm , StaffSignUpTwo,StaffSearchForm
from apps.hostel.models import User ,HostelStaff
from django.contrib.auth import login
from django.shortcuts import redirect
from django.db.models import Q

# Create your views here.
class WardenHomeView(ListView):
    template_name = 'warden_view/warden_home.html'

    def get(self,request):
        data=HostelStaff.objects.all()
        return render(request,self.template_name,{"data":data})

def StaffSignUpView(request):
    if request.method == 'POST':
        main_form = StaffSignUpForm(request.POST)
        secondary_form = StaffSignUpTwo(request.user,request.POST)
        if main_form.is_valid() and secondary_form.is_valid():
            user = main_form.save()
            secondary_form.save(user)
            return redirect('warden-home')
    else:
        main_form = StaffSignUpForm()
        secondary_form = StaffSignUpTwo(request.user)
    return render(request, 'warden_view/create_staff.html', {
        'main_form': main_form,
        'secondary_form': secondary_form
    })

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

def WardenCreateNotice(request):
    res=render(request,'warden_view/create_notice.html')
    return res

def WardenPayView(request):
    res=render(request,'warden_view/warden_payment.html')
    return res
