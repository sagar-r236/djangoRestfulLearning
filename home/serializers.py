from rest_framework import serializers
from home import models


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Color
        fields = ['color_name']
        

class PersonSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    class Meta:
        model = models.Person
        fields = "__all__"
        depth = 1

    def validate(self, data):

        special_character = '!@#$%^&*()_-+=<>,./?\'":;{}][|\\'
        if any(c in special_character for c in data['name']):
            raise serializers.ValidationError('name cannot contain special character')

        if data['age'] < 18:
            raise serializers.ValidationError('age should be greater than 18')
        return data
    

