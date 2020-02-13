from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('admin-home')
        elif request.user.is_warden:
            return redirect('warden-home')
        elif request.user.is_hostelstaff:
            return redirect('staff-home')
        elif request.user.is_parent:
            return redirect('parent-home')

        else:
            return redirect('student-home')
    return render(request, 'classroom/vkarma_landing.html')

"""def about(request):
    return render(request, 'classroom/about.html', {})

def terms_conditions(request):
    return render(request, 'classroom/terms_conditions.html', {})

def privacy_policy(request):
    return render(request, 'classroom/privacy_policy.html', {})
    """
