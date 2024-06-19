from django import forms
from django.contrib.auth.models import User
from demoapp.models import EmployeeModel
from django.contrib.auth.hashers import make_password



class RegisterForm(forms.ModelForm):

    class Meta:
        model=EmployeeModel
        fields = ['first_name', 'last_name', 'username', 'email','age', 'password', 'phone', 'department', 'designation']
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            "username": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}),
            "email": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            "age": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'age'}),
            "password": forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            "phone": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            "department": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}),
            "designation": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Designation'}),
        }
class EmpLoginForm(forms.ModelForm):
    
    class Meta:
        model = EmployeeModel
        fields = ["username","password"]
        widgets={
            "username": forms.TextInput(attrs={'class': 'form-control form-control-custom', 'placeholder': 'User Name','style':'margin-bottom: 20px;'}),
            "password": forms.PasswordInput(attrs={'class': 'form-control form-control-custom', 'placeholder': 'Password','style':'margin-bottom: 20px;'}),
            
        }
        

class EmpEditForm(forms.ModelForm):

    class Meta:
        model=EmployeeModel
        fields = ['first_name', 'last_name', 'username', 'email','age', 'password', 'phone', 'department', 'designation']
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            "username": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}),
            "email": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            "age": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'age'}),
            "password": forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            "phone": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            "department": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}),
            "designation": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Designation'}),
        }
    def clean_password(self):
        # Hash the password before saving
        raw_password = self.cleaned_data['password']
        return make_password(raw_password)
