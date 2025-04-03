from rest_framework import serializers

from users.serializers import UserSerializer

from network.models import Contacts, NetworkNode, Product


class ContactsSerializer(serializers.ModelSerializer):
    """Сериализатор для модели контактов"""
    class Meta:
        model = Contacts
        fields = ["id", "email", "country", "city", "street", "house_number", "user"]
        read_only_fields = ["user"]

    def create(self, validated_data):
        # Автоматически добавляем текущего пользователя
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для модели продуктов"""
    class Meta:
        model = Product
        fields = ["id", "name", "model", "release_date", "user"]
        read_only_fields = ["user"]

    def create(self, validated_data):
        # Автоматически добавляем текущего пользователя
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class NetworkNodeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели сетей"""
    products = ProductSerializer(many=True, read_only=True)
    contacts = ContactsSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = NetworkNode
        fields = ["id", "name", "level", "contacts", "products", "supplier", "debt", "created_at", "user"]
        read_only_fields = ["debt", "user"]  # Запрещаем обновление полей debt и user

    def create(self, validated_data):
        # Автоматически добавляем текущего пользователя
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
