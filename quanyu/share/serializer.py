from rest_framework import serializers
from .models import submmit
class shareserializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=100)
   # image = serializers.CharField(required=True, max_length=500)
    content = serializers.CharField(required=True)
    author = serializers.CharField(required=True)
    time=serializers.TimeField(required=True)
    def create(self, validated_data):
        return submmit.objects.create(**validated_data)
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.value = validated_data.get('value', instance.value)
    #
    #     instance.save()
    #     return instance
class Myshareserializer(serializers.Serializer):
    class Meta:
        model = submmit
        fields = ('title','content','author','time','touxiang')