from django.shortcuts import render
from django.views.generic import ListView
from apps.hostel.forms import StudentSignUpForm,StudentSignUpTwo, StudentSearchForm
from apps.hostel.models import User ,Student
from django.contrib.auth import login
from django.shortcuts import redirect
from django.db.models import Q

# Create your views here.
class StudentHomeView(ListView):
    template_name = 'student_view/student_home.html'

    def get(self,request):
        return render(request,self.template_name)




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
        form=StaffSearchForm(request.POST)

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
