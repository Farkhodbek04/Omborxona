from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryCRUDview, UnitCRUDview, SetStorekeeperView, ProductCRUDView, ProductInputView, ProductOutputView

router = DefaultRouter()
router.register(r'categories', CategoryCRUDview, basename='category')
router.register(r'units', UnitCRUDview, basename='unit')


urlpatterns = [
    path('', include(router.urls)),
    path('storekeepers/', SetStorekeeperView.as_view(), name='storekeeper-list'), # get list of all storekeepers
    path('storekeepers/<int:pk>/', SetStorekeeperView.as_view(), name='storekeeper-detail'), # Update, delete, get specific storekeeper with id
    path('product/', ProductCRUDView.as_view() ), # get all products
    path('product/<int:pk>/', ProductCRUDView.as_view()), # Update, delete, get product with id

]
