from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from users.permissions import IsActiveUser
from network.models import Product, Contacts, NetworkNode
from network.paginators import MyCustomPagination

from network.serializers import ContactsSerializer, NetworkNodeSerializer, ProductSerializer


class ContactsViewSet(ModelViewSet):
    """Контроллер для представления контактов"""
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    pagination_class = MyCustomPagination
    permission_classes = [IsActiveUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["country", "city"]

    def perform_create(self, serializer):
        # Передаем текущего пользователя в сериализатор
        serializer.save(user=self.request.user)


class ProductViewSet(ModelViewSet):
    """Контроллер для представления продуктов"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = MyCustomPagination
    permission_classes = [IsActiveUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "model"]

    def perform_create(self, serializer):
        # Передаем текущего пользователя в сериализатор
        serializer.save(user=self.request.user)


class NetworkNodeViewSet(ModelViewSet):
    """Контроллер для представления сетей"""
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    pagination_class = MyCustomPagination
    permission_classes = [IsActiveUser]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ["contacts__country"]  # Фильтрация по стране
    ordering_fields = ["name", "created_at"]  # Сортировка по имени и дате создания
    search_fields = ["name"]  # Возможность поиска по имени

    def perform_create(self, serializer):
        # Передаем текущего пользователя в сериализатор
        serializer.save(user=self.request.user)
