from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

monthly_challanges = {
    "january": "Complete django",
    "febraury": "Start learning Rust programming",
    "march": "Get a quick job"
}


def challange_by_num(request, month):
    months = list(monthly_challanges.keys())
    redirect_month = months[month]
    return HttpResponseRedirect(f'/challanges/{redirect_month}')


def index(request, month):
    try:
        challange = monthly_challanges[month]
        return HttpResponse(challange)
    except:
        return HttpResponseNotFound("This month is not found")
