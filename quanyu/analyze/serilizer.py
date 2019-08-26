from rest_framework import serializers
from .models import customer_age,customer_staytime,customer_tools,customer_team,customer_method,customer_from
#step1游客年龄
class customerage_Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    value = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return customer_age.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.value = validated_data.get('value', instance.value)
        instance.save()
        return instance


class Mycustomerage_Serializer(serializers.ModelSerializer):
    class Meta:
        model = customer_age
        fields = ['name', 'value']
#step2消费水平
class customerteam_Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    value = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return customer_team.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.value = validated_data.get('value', instance.value)
        instance.save()
        return instance


class Mycustomerteam_Serializer(serializers.ModelSerializer):
    class Meta:
        model = customer_team
        fields = ['name', 'value']
#step3游客停留时间
class customerstaytime_Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    value_1 = serializers.IntegerField(required=True)
    value_2 = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return customer_staytime.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.value_1 = validated_data.get('value', instance.value_1)
        instance.value_2 = validated_data.get('value', instance.value_2)
        instance.save()
        return instance


class Mycustomerstaytime_Serializer(serializers.ModelSerializer):
    class Meta:
        model = customer_staytime
        fields = ['name', 'value_1','value_2']
#step4各地游客数量
class customerfrom_Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name=serializers.CharField(required=True, max_length=100)
    value=serializers.IntegerField(required=True)
    def create(self, validated_data):
        return customer_from.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name= validated_data.get('name', instance.name)
        instance.value = validated_data.get('value', instance.value)
        instance.save()
        return instance
class Mycustomerfrom_Serializer(serializers.ModelSerializer):
    class Meta:
        model = customer_from
        fields = ['name','value']
#step5
class customermethod_Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    value = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return customer_method.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.value = validated_data.get('value', instance.value)
        instance.save()
        return instance


class Mycustomermethod_Serializer(serializers.ModelSerializer):
    class Meta:
        model = customer_method
        fields = ['name', 'value']
#step6
class customertools_Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    value = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return customer_tools.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.value = validated_data.get('value', instance.value)
        instance.save()
        return instance


class Mycustomertools_Serializer(serializers.ModelSerializer):
    class Meta:
        model = customer_tools
        fields = ['name', 'value']

