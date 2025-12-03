from django.urls import path
from . import views

urlpatterns = [
    path("", views.notes_home, name="notes_home"),
    path("create/", views.create_note, name="create_note"),

    path("pin/<int:id>/", views.pin_note, name="pin_note"),
    path("unpin/<int:id>/", views.unpin_note, name="unpin_note"),

    path("archive/<int:id>/", views.archive_note, name="archive_note"),
    path("unarchive/<int:id>/", views.unarchive_note, name="unarchive_note"),

    path("delete/<int:id>/", views.delete_note, name="delete_note"),
    path("restore/<int:id>/", views.restore_note, name="restore_note"),
]
