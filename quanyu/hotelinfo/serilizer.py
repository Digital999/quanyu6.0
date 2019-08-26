from rest_framework import serializers
from .models import hotel,hotelinfo
# class hotelSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     nowman = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     def create(self, validated_data):
#         return hotel.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         instance.name= validated_data.get('name', instance.name)
#         instance.nowman = validated_data.get('nowman', instance.nowman)
#         instance.save()
#         return instance
class MyhotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = hotel
        fields = ('name','nowman')
class hotelinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = hotelinfo
        fields = '__all__'