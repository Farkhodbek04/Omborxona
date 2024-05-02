from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryCRUDview, UnitCRUDview

router = DefaultRouter()
router.register(r'categories', CategoryCRUDview, basename='category')
router.register(r'units', UnitCRUDview, basename='unit')


urlpatterns = [
    path('', include(router.urls)),
]
