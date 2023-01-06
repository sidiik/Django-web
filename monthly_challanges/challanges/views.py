from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime

# Create your views here.

monthly_challanges = {
    "january": "Complete django",
    "febraury": "Start learning Rust programming",
    "march": "Get a quick job"
}


def index(request):
    months = list(monthly_challanges.keys())
    list_months = ""

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challange", args=[month])

        list_months += f"<li> <a href=\"{month_path}\">{capitalized_month}</a> </li>"

    response_data = f"<ul> {list_months} </ul>"

    return HttpResponse(response_data)


def challange_by_num(request, month):
    months = list(monthly_challanges.keys())
    if month > len(months) or (month == 0):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challange", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def challanges_by_name(request, month):
    try:
        challange = monthly_challanges[month]
        return HttpResponse(challange)
    except:
        return HttpResponseNotFound("This month is not found")


def display_date(request):
    year = datetime.today().year
    return HttpResponse(year)
