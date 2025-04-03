from django.urls import path, include
from rest_framework.routers import DefaultRouter

from network import views

app_name = 'network'

router = DefaultRouter()
router.register(r"networks", views.NetworkNodeViewSet, basename="networks")
router.register(r"products", views.ProductViewSet, basename="products")
router.register(r"contacts", views.ContactsViewSet, basename="contacts")

urlpatterns = [
    path("", include(router.urls)),

]
