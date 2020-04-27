from django.contrib import admin
from django.urls import path
import app.views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.home, name='home')
]
