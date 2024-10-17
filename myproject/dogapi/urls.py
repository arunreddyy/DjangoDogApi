from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'dogs', views.DogViewSet)
router.register(r'breeds', views.BreedViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
