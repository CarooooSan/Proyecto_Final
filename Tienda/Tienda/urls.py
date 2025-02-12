"""Tienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from api.views import Home, stats, tables, forgot

from api import views

urlpatterns = [
    # path('admin/', admin.site.urls),
  
    path('',Home.as_view(),name='index'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('stats/',stats.as_view(),name='stats'),
    path('tables/',tables.as_view(),name='tables'),
    path('forgot/',views.forgotPwd,name='forgot'),
    path('logout/',views.signout,name='logout'),
    path('enviar_correo/<str:correo>/<str:contra>/', views.enviar_correo, name='enviar_correo'),
        
]
