from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("upload/", views.upload, name="upload"),
    path("upload/health/", views.upload_health, name="upload_health"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("parents/", views.parents, name="parents"),
    path("attendances/", views.attendances, name="attendances"),
    path("events/", views.events, name="events"),
    path('view/<int:event_id>', views.view_event, name='view_event'),
    path("events/edit/<int:event_id>/", views.edit_event, name="edit_event"),
    path("events/delete/<int:event_id>/", views.delete_event, name="delete_event"),
]
