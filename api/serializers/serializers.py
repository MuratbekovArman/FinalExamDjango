from datetime import datetime

from rest_framework import serializers

from api.models import Category, Sale, Appeal


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image')

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Invalid name!')
        return value


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('id', 'name', 'description', 'date', 'image')

    def validate_date(self, value):
        if value < datetime.today():
            raise serializers.ValidationError('Date cannot be in the past!')
        return value

    def validate_name(self, value):
        if 'buy' in value:
            raise serializers.ValidationError('Name cannot contain buy word')
        return value


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = ('id', 'title', 'file', 'is_active')
