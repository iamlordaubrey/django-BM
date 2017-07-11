from rest_framework import viewsets
from .models import OrganizationUnit
from .serializers import OrganizationUnitSerializer


class OrganizationUnitViewSet(viewsets.ModelViewSet):
    queryset = OrganizationUnit.objects.all()
    serializer_class = OrganizationUnitSerializer
