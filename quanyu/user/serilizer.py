from rest_framework import serializers
from .models import userinfo
class userinfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True, allow_blank=False, max_length=100)
    images = serializers.CharField(required=True, allow_blank=False, max_length=100)
    location = serializers.CharField(required=True, allow_blank=False, max_length=100)
    openid = serializers.CharField(required=True,max_length=100)
    def create(self, validated_data):
        return userinfo.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.username= validated_data.get('username', instance.username)
        instance.images = validated_data.get('images', instance.images)
        instance.location = validated_data.get('location', instance.location)
        instance.openid = validated_data.get('openid', instance.openid)
        instance.save()
        return instance
class TelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = userinfo
        fields = '__all__'
