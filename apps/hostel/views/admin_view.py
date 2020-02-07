from django.shortcuts import render
from django.views.generic import ListView
from apps.hostel.forms import WardenSignUpForm,WardenSignUpTwo, WardenSearchForm
from apps.hostel.models import User ,Warden
from django.contrib.auth import login
from django.shortcuts import redirect
from django.db.models import Q
# Create your views here.
class AdminHomeView(ListView):
    template_name = 'admin_view/admin_home.html'

    def get(self,request):
        data=Warden.objects.all()
        return render(request,self.template_name,{"data":data,})

def WardenSignUpView(request):
    if request.method == 'POST':
        main_form = WardenSignUpForm(request.POST)
        secondary_form = WardenSignUpTwo(request.user,request.POST)
        if main_form.is_valid() and secondary_form.is_valid():
            user = main_form.save()
            secondary_form.save(user)
            return redirect('admin-home')
    else:
        main_form = WardenSignUpForm()
        secondary_form = WardenSignUpTwo(request.user)
    return render(request, 'admin_view/create_warden.html', {
        'main_form': main_form,
        'secondary_form': secondary_form
    })

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

def AdminCreateNotice(request):
    res=render(request,'admin_view/create_notice.html')
    return res

def WardenLoginView(request):
    res=render(request,'admin_view/login_warden.html')
    return res
