"""
URL configuration for SmartSubsidySystemDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import Home, Login, Register, logoutuser, Aboutus, Contactus, Services, Scheme1, Dash, Applicationform, Approval, subsidy
from django.urls import path
from .views import subsidy_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', Home, name='homepage'),
    path('loginpage/', Login, name='loginpage'),
    path('', Register, name='register'),
    path('logout_user/',logoutuser, name='logout_user'),
    path('aboutus/',Aboutus, name='aboutus'),
    path('contactus/', Contactus, name='contactus'),
    path('services/',Services, name='services'),
    path('scheme1/',Scheme1, name='scheme1'),
    path('Schemesinfo/',Dash, name='Dash'),
    path('applicationform/',Applicationform, name='applicationform'),
    path('approval/',Approval, name='approval'),
    path('homepage/subsidy.html', subsidy_view, name='subsidy_view'),

]
