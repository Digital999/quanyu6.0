from rest_framework import serializers
from .models import scenic
class scenicinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = scenic
        fields = '__all__'