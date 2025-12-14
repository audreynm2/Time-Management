from rest_framework.routers import DefaultRouter
from .views import ObjectiveViewSet

router = DefaultRouter()
# Register the ViewSet. 
router.register(r'objectives', ObjectiveViewSet)

urlpatterns = router.urls