"""
URL configuration for business_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app1 import views
admin.site.site_header = "Bharat IT Solutions"            
admin.site.site_title = "Bharat IT Admin Portal"          
admin.site.index_title = "Web & Software Development"  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup, name='signup'),
    path('login', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/',views.LogoutPage, name='logout'),
    path('about/', views.about, name='about'),
    path('services/',views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('saveform/',views.save_form, name='saveform'),
    path('project/', views.project, name='project'),
    path('get_quote/', views.get_quote, name='getquote'),
]
