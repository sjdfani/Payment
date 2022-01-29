from rest_framework import serializers
from .models import Demands


class DemandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demands
        fields = '__all__'
        extra_kwargs = {
            'user': {
                'required': False
            }
        }

    def validate_price(self, value: str):
        if not value.isnumeric():
            raise serializers.ValidationError('price should be number.')
        return value
