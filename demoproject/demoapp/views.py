
from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from demoapp.models import EmployeeModel
from .forms import RegisterForm,EmpLoginForm,EmpEditForm
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

# To view homepage
class HomeView(View):
    def get(self,request):
        return render(request,'home.html')
    
# to view user home after login successful
class UserHome(View):
    def get(self,request):
        return render(request,'user_home.html')
    
# To view registration form and add db 
class EmployeeRegisterView(CreateView):
    model = EmployeeModel
    form_class=RegisterForm
    template_name = "register.html"
    success_url=reverse_lazy('home_view')
    def form_valid(self, form):
        EmployeeModel.objects.create_user(**form.cleaned_data)
        return redirect('home_view')
    
#    To login and authentication 
class EmpLoginView(View):
    def get(self,request):
        form=EmpLoginForm()
        return render(request,'login.html',{"form":form})
    def post(self,request):
        uname=request.POST.get("username")
        psw=request.POST.get("password")
        user=authenticate(request,username=uname,password=psw)
        if user:
            login(request,user)
            messages.success(request, "Login successful.")
            return render(request,'user_home.html')
        else:
            messages.error(request, "invalid credentials.")
            return redirect('home_view')
        
#    To logout     
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('home_view')
    
# To view the details of the Employee
class EmpProfileView(View):
    def get(self,request,*args, **kwargs):
        user=EmployeeModel.objects.filter(username=request.user)
        return render(request,'emp_profile.html',{'data':user})
    
# To edit the Employee details  
class EmpEditView(UpdateView):
    model=EmployeeModel
    form_class=EmpEditForm
    template_name='emp_profile_edit.html'
    success_url=reverse_lazy('user_home')
    pk_url_kwarg='id'
    
    
#   To delete the employee details  
class EmpDeleteView(DeleteView):
    model=EmployeeModel
    pk_url_kwarg='id'
    success_url=reverse_lazy('user_home')
    template_name='delete_view.html'
            

    

  