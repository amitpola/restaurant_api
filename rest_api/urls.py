from django.urls import path, include
from.views import RestaurantViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'restaurants/add_new_restaurants',RestaurantViewSet)


urlpatterns = [
    path('',include(router.urls)),
]