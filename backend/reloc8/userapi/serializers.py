from userapi.models import Client
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'vehicle', 'ent_val', 'housing','din_out', 'salary', 'city_new')

class ProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'salary', 'city_new')