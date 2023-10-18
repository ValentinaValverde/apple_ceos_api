from rest_framework import serializers
from .models import AppleCeo

class AppleCeoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppleCeo
        fields = ['name', 'first_year_active']
