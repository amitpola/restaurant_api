from rest_framework import serializers
from .models import Restaurant
#creating serializer for Restaurant

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"

