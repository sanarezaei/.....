from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r"accounts", AccountViewSet)
router.register(r"profiles", ProfileViewSet, basename="profile")

urlpatterns = router.urls