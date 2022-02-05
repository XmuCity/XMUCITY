from django.urls import path,include
from plform.views.index import index

urlpatterns = [
        path("", index, name="index"),
        path("menu/", include("plform.urls.menu.index")),
        path("playground/", include("plform.urls.playground.index")),
        path("settings/", include("plform.urls.settings.index"))
]

