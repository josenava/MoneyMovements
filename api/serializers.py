from rest_framework import serializers
from api.models import Category, Transaction
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


class TransactionSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True
    )

    class Meta:
        model = Transaction
        fields = ('id', 'description', 'amount', 'date', 'categories', 'user')

    def create(self, validated_data):
        user_categories = Category.objects.filter(user=validated_data['user'])
        transaction = Transaction(
            description=validated_data['description'],
            amount=validated_data['amount'],
            date=validated_data['date'],
            user=validated_data['user']
        )
        transaction.save()
        transaction.categories.set(self.categorize_movement(movement.description, user_categories))
        transaction.save()

        return transaction

    def validate_categories(self, categories):
        for category in categories:
            if category.user.id != self.context['request'].user.id:
                raise serializers.ValidationError('There is at least one category which does not belong to the user')

        return categories

    def categorize_transaction(self, description, user_categories):
        """
        :param description: transaction description
        :param user_categories: list of categories by user
        :return: assigns transaction to user categories
        """
        transaction_categories = []

        for category in user_categories:
            category_related_words = category.related_words.split(';')
            for crw in category_related_words:
                if description.lower().find(crw.lower()) != -1:
                    transaction_categories.append(category)
                    break

        return transaction_categories
