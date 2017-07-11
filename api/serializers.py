from rest_framework import serializers
from .models import OrganizationUnit


class OrganizationUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationUnit
