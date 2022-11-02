
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

