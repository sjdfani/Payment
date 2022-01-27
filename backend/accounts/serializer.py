from rest_framework import serializers
from .models import AccountModel


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = '__all__'

    def validate_price(self, value: str):
        if not value.isnumeric():
            raise serializers.ValidationError('price should be number.')
        return value
