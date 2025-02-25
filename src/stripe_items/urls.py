from django.urls import path

from .views import buy, get_item

urlpatterns = [
    path('buy/<int:pk>', buy),
    path('items/<int:pk>', get_item),
]