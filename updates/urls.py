from django.conf.urls import url
from django.contrib import admin
from updates.views import (
    json_example_view,
    JSONCBV,
    SerializedListView
)

urlpatterns = [
    url(r'^updatefuncview/', json_example_view),
    url(r'^updatecbv/', JSONCBV.as_view()),
    url(r'^updateserializedcbv/', SerializedListView.as_view()),
]
