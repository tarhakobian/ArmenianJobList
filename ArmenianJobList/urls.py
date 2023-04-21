"""
URL configuration for ArmenianJobList project.

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

import core.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', core.views.home, name='home'),
    path('profile/', core.views.profile, name='profile'),
    path('post/<str:post_id>/', core.views.post_details, name='post_details'),
    path('login/', core.views.login_page, name='login'),
    path('register/', core.views.register_page, name='register')
]
