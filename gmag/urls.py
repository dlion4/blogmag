"""
URL configuration for gmag project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import  views


urlpatterns = [
    path('about-us/', views.AboutUs.as_view(), name="about"),
    path('contact-us/', views.ContactUs.as_view(), name="contact"),
    path('lionnic-admin-login/', admin.site.urls),
    path('', include("posts.urls", namespace="posts")),
    path('category/', include("category.urls", namespace="category")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("writer/", include("writer.urls", namespace="writer")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = "handlers.views.handler404"
handler500 = "handlers.views.handler500"



admin.site.site_header  =  "Lionnic Margazone"  
admin.site.site_title  =  "Lionnic Margazone Admin Site"
admin.site.index_title  =  "Lionnic Margazone Admin Site"