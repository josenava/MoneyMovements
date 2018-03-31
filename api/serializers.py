from rest_framework import serializers
from api.models import Category, Movement
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Category
        fields = ('id', 'name', 'related_words', 'user',)


class MovementSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True
    )

    class Meta:
        model = Movement
        fields = ('id', 'description', 'amount', 'date', 'categories')

    def validate_categories(self, categories):
        user = self.context['request'].user
        for category in categories:
            if category.user.id != user.id:
                raise serializers.ValidationError('There is at least one category which does not belong to the user')

        return categories
