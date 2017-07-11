from django.conf.urls import url
from rest_framework import routers
from api.views import OrganizationUnitViewSet

router = routers.DefaultRouter()
router.register(r'organization-units', OrganizationUnitViewSet)

urlpatterns = router.urls

