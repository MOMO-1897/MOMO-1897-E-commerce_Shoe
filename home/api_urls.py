# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers
from .api_views import *
router = routers.DefaultRouter()
router.register(r'Products', ProductViewSet)
router.register(r'Brands', BrandsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('product_filter', ProductListView.as_view(), name='product_filter'),
    path('product_crud/<int:pk>', ProductDetail.as_view(), name='product_filter'),
]
