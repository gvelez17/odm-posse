"""posse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('odm/admin/', admin.site.urls),

    path('ads/', views.AdListView.as_view(), name='ads'),
    path('odm/ads/', views.AdListView.as_view(), name='odm_ads'),

    path('orgs/', views.OrgListView.as_view(), name='orgs'),
    path('odm/orgs/', views.OrgListView.as_view(), name='odm_orgs'),

    path('ad/<int:pk>', views.AdDetailView.as_view(), name='ad'),
    path('odm/ad/<int:pk>', views.AdDetailView.as_view(), name='odm_ad'),

    path('org/<int:pk>', views.OrgDetailView.as_view(), name='org'),
    path('odm/org/<int:pk>', views.OrgDetailView.as_view(), name='odm_org'),

]
