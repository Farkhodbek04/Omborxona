from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryCRUDview, UnitCRUDview, SetStorekeeperView, ProductCRUDView

router = DefaultRouter()
router.register(r'categories', CategoryCRUDview, basename='category')
router.register(r'units', UnitCRUDview, basename='unit')


urlpatterns = [
    path('', include(router.urls)),
    path('storekeepers/', SetStorekeeperView.as_view(), name='storekeeper-list'),
    path('storekeepers/<int:pk>/', SetStorekeeperView.as_view(), name='storekeeper-detail'),
    path('product/', ProductCRUDView.as_view() ),
    path('product/<int:pk>/', ProductCRUDView.as_view())

]
