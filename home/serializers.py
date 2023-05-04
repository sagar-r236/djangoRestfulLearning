from rest_framework import serializers
from home import models


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Person
        fields = "__all__"

    def validate(self, data):

        special_character = '!@#$%^&*()_-+=<>,./?\'":;{}][|\\'
        if any(c in special_character for c in data['name']):
            raise serializers.ValidationError('name cannot contain special character')

        if data['age'] < 18:
            raise serializers.ValidationError('age should be greater than 18')
        return data
    

