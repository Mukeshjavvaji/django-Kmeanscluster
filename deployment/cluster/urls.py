from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.open_form),
    path('predict', views.predict)
]