from django.urls import path
from plform.views import index

urlpatterns = {
        path("", index, name="index"),
}

