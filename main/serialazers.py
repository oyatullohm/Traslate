from rest_framework import serializers
from .models import  Trans

class TransSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trans
        fields =  ['en','ru','uz']
