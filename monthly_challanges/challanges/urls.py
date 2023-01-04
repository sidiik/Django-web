from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>", views.challange_by_num),
    path("<str:month>", views.index)
]
