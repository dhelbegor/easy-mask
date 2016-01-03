# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from apps.core.views import ListView

from apps.core import views


urlpatterns = [
    url(r'^$', ListView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)