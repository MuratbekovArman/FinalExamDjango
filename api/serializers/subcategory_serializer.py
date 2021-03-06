from rest_framework import serializers

from api.models import Sub_category


class SubCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    image = serializers.CharField()
    category_id = serializers.IntegerField()

    def create(self, data):
        sub_category = Sub_category.objects.create(name=data.get(['name']))
        return sub_category

    def update(self, instance, data):
        instance.name = data.get['name']
        instance.save()
        return instance

    def validate_name(self, value):
        if value.isupper():
            raise serializers.ValidationError('Name cannot be in capital letters!')
