from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from django.urls import reverse

# Create your views here.

monthly_challanges = {
    "january": "Complete django",
    "febraury": "Start learning Rust programming",
    "march": "Get a quick job"
}


def challange_by_num(request, month):
    months = list(monthly_challanges.keys())
    if month > len(months) or (month == 0):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challange", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def index(request, month):
    try:
        challange = monthly_challanges[month]
        return HttpResponse(challange)
    except:
        return HttpResponseNotFound("This month is not found")
