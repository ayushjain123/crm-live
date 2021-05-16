"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    )
from leads.views import landing, LandingPageView, SignupView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LandingPageView.as_view(), name='landing_page'),
    path('leads/', include('leads.urls')),
    path('agents/', include('agents.urls')),
    path('signup/',SignupView.as_view(), name='signup'),
    path('reset/',PasswordResetView.as_view(), name='reset'),
    path('reset_done/',PasswordResetDoneView.as_view(), name='reset_done'),
    path('reset_confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='reset_confirm'),
    path('reset_complete/',PasswordResetCompleteView.as_view(), name='reset_complete'),    
    path('login/',LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout')
]
urlpatterns= urlpatterns + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
