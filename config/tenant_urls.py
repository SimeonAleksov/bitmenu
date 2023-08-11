from django.urls import include
from django.urls import path

urlpatterns = [
    path('menus/', include('apps.menus.application.urls', namespace='menus')),
]
