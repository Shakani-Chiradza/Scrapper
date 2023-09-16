from django.shortcuts import render
from .models import scrappedData
from django.http import HttpResponse
from .scrapping_function import scrape_property_data

# Create your views here.


def index(request):
    return HttpResponse("<h1>App is running</h1>")


def add_record(request):
    properties = scrape_property_data()
    for i in properties:
        scrappedData.insert_one(i)
    return HttpResponse("New record added")


def get_records(request):
    recorded = scrappedData.find()
    return HttpResponse(recorded)

