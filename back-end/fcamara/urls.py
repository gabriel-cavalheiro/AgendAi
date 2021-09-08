from django.contrib import admin
from django.urls import path, include
from agendai import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

]
