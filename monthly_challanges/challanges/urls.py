from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, ),
    path("date", views.display_date),
    path("<int:month>", views.challange_by_num),
    path("<str:month>", views.challanges_by_name, name="month-challange"),
]
