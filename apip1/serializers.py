
from rest_framework import serializers
from . models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class DummySerializer(serializers.Serializer):
    clas = serializers.CharField()
    section = serializers.CharField(required=False)


    # optional_fields = ['section', ]
    # def get_validation_exclusions(self):
    #     exclusions = super(DummySerializer, self).get_validation_exclusions()
    #     return exclusions + ['section']


class SummySerializer(serializers.Serializer):
    room = serializers.CharField()
    numb = serializers.CharField(required=False)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class BossSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boss
        fields = "__all__"


class Boss2Serializer(BossSerializer):
    favemp = EmployeeSerializer(required=False)


class WorkSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(required=False)
    in_dept = serializers.CharField(required=False)
    boss = Boss2Serializer(required=False)











