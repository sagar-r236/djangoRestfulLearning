from rest_framework import serializers
from home import models


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Person
        fields = "__all__"