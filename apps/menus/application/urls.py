from django.urls import path

from apps.menus.application import views

app_name = 'menus'

urlpatterns = [
    path(
        'list/',
        view=views.UserList.as_view(),
        name='detail',
    ),
]
