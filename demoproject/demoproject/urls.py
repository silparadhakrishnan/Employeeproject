"""
URL configuration for demoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from demoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(),name="home_view"),
    path('userhome',views.UserHome.as_view(),name="user_home"),
    path('reg',views.EmployeeRegisterView.as_view(),name="reg_view"),
    path('log',views.EmpLoginView.as_view(),name="login_view"),
    path("logout",views.LogoutView.as_view(),name="logout_view"),
    path('pro',views.EmpProfileView.as_view(),name="profile_view"),
    path('edit/<int:id>',views.EmpEditView.as_view(),name="edit_view"),
    path('delete/<int:id>',views.EmpDeleteView.as_view(),name="delete_view")
]
