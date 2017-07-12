from django.conf.urls import url, include
from rest_framework import routers
from api.views import OrganizationUnitViewSet

from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'org-units', OrganizationUnitViewSet)

docs = get_swagger_view(title='CIS API')

urlpatterns = [
    url(r'^docs/', docs),
]

urlpatterns += router.urls

