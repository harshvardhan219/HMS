from django.shortcuts import render
from django.views.generic import ListView
from apps.hostel.forms import StudentSignUpForm,StudentSignUpTwo, StudentSearchForm
from apps.hostel.models import User ,Student
from django.contrib.auth import login
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from ..decorators import student_required, admin_required,hostelstaff_required
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

# Create your views here.

class StudentHomeView(ListView):
    template_name = 'student_view/student_home.html'

    def get(self,request):
        return render(request,self.template_name)

class StudentUpdateView(BSModalUpdateView):
    model = Student
    template_name = 'staff_view/update_student.html'
    form_class = StudentSignUpTwo
    success_message = 'Success: Student was updated.'
    success_url = reverse_lazy('staff_view:staff-home')

class StudentDeleteView(BSModalDeleteView):
    model = User
    context_object_name = 'field'
    template_name = 'staff_view/delete_student.html'
    success_message = 'Success: Student was deleted.'
    success_url = reverse_lazy('staff_view:staff-home')

class StudentReadView(BSModalReadView):
    model = Student
    context_object_name = 'field'
    template_name = 'staff_view/read_student.html'




@login_required
@hostelstaff_required
def StudentSignUpView(request):
    if request.method == 'POST':
        main_form = StudentSignUpForm(request.POST)
        secondary_form = StudentSignUpTwo(request.user,request.POST)
        if main_form.is_valid() and secondary_form.is_valid():
            user = main_form.save()
            secondary_form.save(user)
            return redirect('staff_view:staff-home')
    else:
        main_form = StudentSignUpForm()
        secondary_form = StudentSignUpTwo(request.user)
    return render(request, 'staff_view/create_student.html', {
        'main_form': main_form,
        'secondary_form': secondary_form
    })

def StudentSearchView(request):
    if request.method == 'POST':
        form=StudentSearchForm(request.POST)

        data=Student.objects.filter(Q(firstName__icontains=form.data['search']) | Q(lastName__icontains=form.data['search']) | Q(hostel_name__icontains=form.data['search']))
        res=render(request,'staff_view/search_student.html',{'form':form,'data':data})
        return res

    else:
        form=StudentSearchForm()
        res=render(request,'staff_view/search_student.html',{'form':form})
        return res


def StaffPayView(request):
    res=render(request,'staff_view/staff_payment.html')
    return res

def StudentAttandanceView(request):
    res=render(request,'student_view/attendance.html')
    return res
