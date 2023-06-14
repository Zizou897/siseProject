from django.urls import path

from app.api import Liste_Dernier_Prix


urlpatterns = [
    path('liste-dernier-prix-marche/', Liste_Dernier_Prix.as_view() ),
]
