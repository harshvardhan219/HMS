from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    is_warden = models.BooleanField(default=False)
    is_hostelstaff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Warden(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstName = models.CharField(max_length=30,null=True)
    lastName = models.CharField(max_length=30,null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=12 ,null=True)
    hostel_name=models.CharField(max_length=20,null=True)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.email


class HostelStaff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstName = models.CharField(max_length=30,null=True)
    lastName = models.CharField(max_length=30,null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=12 ,null=True)
    hostel_name=models.CharField(max_length=100)
    warden = models.ForeignKey(Warden, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.email

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstName = models.CharField(max_length=30,null=True)
    lastName = models.CharField(max_length=30,null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=12,null=True)
    hostel_name=models.CharField(max_length=100,null=True)
    parent_name=models.CharField(max_length=100,null=True)
    class_name=models.CharField(max_length=100,null=True)
    roll_number=models.CharField(max_length=10 ,null=True)
    staff = models.ForeignKey(HostelStaff, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.user.firstName + ' ' + self.user.lastName

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstName = models.CharField(max_length=30,null=True)
    lastName = models.CharField(max_length=30,null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=12 ,null=True)
    hostel_name=models.CharField(max_length=100,null=True)
    childern_name = models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    child = models.ForeignKey(Student, on_delete=models.CASCADE)
    staff = models.ForeignKey(HostelStaff, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.firstName + ' ' + self.user.lastName

class Noticee(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE,related_name='sender')
    issue_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='reciever')
    Subject = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    file = models.FileField(upload_to='notice_files', blank=True)

    def __str__(self):
           return self.name




class Notification(models.Model):
    pass

class Message(models.Model):
    pass
class Request(models.Model):
    pass

class Attendence(models.Model):
    pass
