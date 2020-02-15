from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from crispy_forms.helper import FormHelper
from apps.hostel.models import  User,Warden,HostelStaff,Student,Noticee
from bootstrap_modal_forms.forms import BSModalForm
import datetime
import time
import random
from django.db.models.fields import TimeField
from bootstrap_datepicker_plus import DateTimePickerInput


#admin relatd form
class WardenSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',)

    def save(self):
        user = super().save(commit=False)
        user.is_warden = True
        user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(WardenSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = ' username'
        self.fields['password1'].widget.attrs['placeholder'] = ' password'
        self.fields['password2'].widget.attrs['placeholder'] = ' confirm password'
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for fieldname in ['username','password1', 'password2']:
            self.fields[fieldname].help_text = None


class WardenSignUpTwo(BSModalForm):
    class Meta:
        model = Warden
        fields = ('firstName', 'lastName','email', 'phone_number', 'hostel_name')

    def __init__(self, user, *args, **kwargs):
        super(WardenSignUpTwo, self).__init__(*args, **kwargs)
        self.fields['firstName'].widget.attrs['placeholder'] = ' first name'
        self.fields['lastName'].widget.attrs['placeholder'] = ' last name'
        self.fields['hostel_name'].widget.attrs['placeholder'] = ' hostel name'
        self.fields['email'].widget.attrs['placeholder'] = ' email'
        self.fields['phone_number'].widget.attrs['placeholder'] = ' phone '

        self.helper = FormHelper()
        self.helper.form_show_labels = False


    def save(self, user):
        self.fields['user'] = user
        firstName = self.cleaned_data['firstName']
        lastName = self.cleaned_data['lastName']
        email = self.cleaned_data['email']
        phone_number = self.cleaned_data['phone_number']
        hostel_name = self.cleaned_data['hostel_name']
        warden = Warden.objects.create(user=user,  email=email,firstName=firstName,lastName=lastName,
                                       phone_number=phone_number,hostel_name=hostel_name)

class WardenSearchForm(forms.Form):
     search = forms.CharField(label='',
                    widget=forms.TextInput(attrs={'placeholder': '  Enter warden name  or hostel name'}))


#Warden related form
class StaffSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',)

    def save(self):
        user = super().save(commit=False)
        user.is_hostelstaff = True
        user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(StaffSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = ' username'
        self.fields['password1'].widget.attrs['placeholder'] = ' password'
        self.fields['password2'].widget.attrs['placeholder'] = ' confirm password'
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for fieldname in ['username','password1', 'password2']:
            self.fields[fieldname].help_text = None


class StaffSignUpTwo(forms.ModelForm):
    class Meta:
        model = HostelStaff
        fields = ('firstName', 'lastName','email', 'phone_number', 'hostel_name')

    def __init__(self, user, *args, **kwargs):
        super(StaffSignUpTwo, self).__init__(*args, **kwargs)
        self.fields['firstName'].widget.attrs['placeholder'] = ' first name'
        self.fields['lastName'].widget.attrs['placeholder'] = ' last name'
        self.fields['hostel_name'].widget.attrs['placeholder'] = ' hostel name'
        self.fields['email'].widget.attrs['placeholder'] = ' email'
        self.fields['phone_number'].widget.attrs['placeholder'] = ' phone '
        self.helper = FormHelper()
        self.helper.form_show_labels = False


    def save(self, user):
        self.fields['user'] = user
        firstName = self.cleaned_data['firstName']
        lastName = self.cleaned_data['lastName']
        email = self.cleaned_data['email']
        phone_number = self.cleaned_data['phone_number']
        hostel_name = self.cleaned_data['hostel_name']
        staff = HostelStaff.objects.create(user=user,  email=email,firstName=firstName,lastName=lastName,
                                       phone_number=phone_number,hostel_name=hostel_name)

class StaffSearchForm(forms.Form):
     search = forms.CharField(label='',
                    widget=forms.TextInput(attrs={'placeholder': '  Enter staff name  or hostel name'}))

#Staff related form
class StudentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',)

    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(StudentSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = ' username'
        self.fields['password1'].widget.attrs['placeholder'] = ' password'
        self.fields['password2'].widget.attrs['placeholder'] = ' confirm password'
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for fieldname in ['username','password1', 'password2']:
            self.fields[fieldname].help_text = None


class StudentSignUpTwo(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('firstName', 'lastName','email', 'phone_number', 'hostel_name', 'parent_name','class_name','roll_number')

    def __init__(self, user, *args, **kwargs):
        super(StudentSignUpTwo, self).__init__(*args, **kwargs)
        self.fields['firstName'].widget.attrs['placeholder'] = ' first name'
        self.fields['lastName'].widget.attrs['placeholder'] = ' last name'
        self.fields['hostel_name'].widget.attrs['placeholder'] = ' hostel name'
        self.fields['email'].widget.attrs['placeholder'] = ' email'
        self.fields['phone_number'].widget.attrs['placeholder'] = ' phone '
        self.fields['parent_name'].widget.attrs['placeholder'] = ' parent name '
        self.fields['class_name'].widget.attrs['placeholder'] = ' class '
        self.fields['roll_number'].widget.attrs['placeholder'] = ' roll number '
        self.helper = FormHelper()
        self.helper.form_show_labels = False



    def save(self, user):
        self.fields['user'] = user
        firstName = self.cleaned_data['firstName']
        lastName = self.cleaned_data['lastName']
        email = self.cleaned_data['email']
        phone_number = self.cleaned_data['phone_number']
        hostel_name  = self.cleaned_data['hostel_name']
        parent_name  = self.cleaned_data['parent_name']
        class_name   = self.cleaned_data['class_name']
        roll_number  = self.cleaned_data['roll_number']
        student = Student.objects.create(user=user,  email=email,firstName=firstName,lastName=lastName,
                                       phone_number=phone_number,hostel_name=hostel_name,parent_name=parent_name,class_name=class_name,roll_number=roll_number)

class StudentSearchForm(forms.Form):
     search = forms.CharField(label='',
                    widget=forms.TextInput(attrs={'placeholder': '  Enter Student name  or hostel name'}))

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Noticee
        fields = ('Subject','description','users','file',)

    def save(self,user):
        owner = user
        issue_date = datetime.datetime.now().strftime("%Y-%m-%d")
        Subject = self.cleaned_data['Subject']
        description = self.cleaned_data['description']
        users = self.cleaned_data['users']
        file = self.cleaned_data['file']

        Noticee.objects.create(Subject=Subject, description=description, users=users, file=file, owner=owner, issue_date=issue_date)

    def __init__(self, users, *args, **kwargs):
        super(NoticeForm, self).__init__(*args, **kwargs)
        self.fields['users'].queryset = User.objects.filter(is_admin=False)
        self.fields['Subject'].widget.attrs['placeholder'] = ' Subject'
        self.fields['description'].widget.attrs['placeholder'] = ' Enter your msg......'
        self.helper = FormHelper()
        self.helper.form_show_labels = False
