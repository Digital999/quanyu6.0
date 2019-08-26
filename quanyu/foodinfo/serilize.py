from rest_framework import serializers
from .models import food
class foodSerializer(serializers.Serializer):
    pass
    # id = serializers.IntegerField(read_only=True)
    # imgpath = serializers.CharField(required=True, allow_blank=False, max_length=100)
    # title = serializers.CharField(required=True, allow_blank=False, max_length=100)
    # star = serializers.CharField(required=True, allow_blank=False, max_length=100)
    # price = serializers.CharField(required=True, allow_blank=False, max_length=100)
    # distance = serializers.CharField(required=True, allow_blank=False, max_length=100)
    # labels = serializers.CharField(required=True, allow_blank=False, max_length=100)
    # evaluate = serializers.CharField(required=True, allow_blank=False, max_length=100)
    # group = serializers.CharField(required=True, allow_blank=False, max_length=100)
    # coupons = serializers.CharField(required=True, allow_blank=False, max_length=100)
    # def create(self, validated_data):
    #     return food.objects.create(**validated_data)
    # def update(self, instance, validated_data):
    #     instance.name= validated_data.get('name', instance.name)
    #     instance.nowman = validated_data.get('nowman', instance.nowman)
    #     instance.save()
    #     return instance
class foodinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = food
        fields = '__all__'
