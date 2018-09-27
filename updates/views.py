import json
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View

from updates.models import Update

# Create your views here.


def json_example_view(request):
    """
    standard functional JSON response from django
    """

    data = {
        "count": 1000,
        "content": "Some new content"
    }

    return JsonResponse(data)


class JSONCBV(View):
    """
    standard Class Based View (CBV) JSON response from django
    """

    def get(self, request, *args, **kwargs):

        data = {
            "count": 1000,
            "content": "Some new content"
        }

        return JsonResponse(data)


class SerializedListView(View):
    """
    standard Serialized data of model's JSON response from django
    """

    def get(self, request, *args, **kwargs):

        qs = Update.objects.all()

        data = serialize('json', qs)
        # data = serialize('json', qs, fields=('user', 'content'))
        json_data = data

        return HttpResponse(json_data, content_type='application/json')
