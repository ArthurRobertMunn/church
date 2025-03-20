from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("details/<int:person_id>", views.details, name="details"),
    path("update/<int:person_id>/", views.update, name="update"),
    path("delete/<int:person_id>/", views.delete, name="delete"),
    path("search/", views.search, name="search"),
    path("comment/<int:person_id>", views.comment, name="comment"),
]