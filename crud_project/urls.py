"""crud_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from students import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home, name='home'),
    url(r'^show/', views.show, name='show'),
    url(r'^form/', views.user_form, name='form'),
    url(r'^login/', views.login_v, name='login'),
    url(r'^logout/', views.logout_v, name='logout'),
    url(r'^register/', views.register_v, name='register'),
    url(r'^profile/', views.user_prolfie_list, name='profile'),
    url(r'^profile_view/(?P<page>\d+)/(?P<student_id>\d+)/', views.user_prolfie_view, name='null'),
    url(r'^profile_delete/(?P<page>\d+)/(?P<student_id>\d+)/', views.user_prolfie_delete, name='del'),
    url(r'^restart/', views.restart),

    url(r'^profile_view/', views.reditect_to_home, name='home'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
