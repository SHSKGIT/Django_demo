"""listingllama URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django_private_chat import urls as django_private_chat_urls
from django.conf.urls import url
import notifications.urls

urlpatterns = [
    url('', include(django_private_chat_urls)),
    url('', include('django.contrib.auth.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('', include('users.urls', namespace='users_1')),
    path('control/', admin.site.urls),
    url('inbox/notifications/', include(notifications.urls, namespace='notifications')),
]
