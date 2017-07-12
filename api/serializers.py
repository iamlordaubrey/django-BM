from rest_framework import serializers
from .models import OrganizationUnit
import uuid


class OrganizationUnitSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        extra_kwargs = {
            'organization_business_id': {'read_only': True}
        }
        model = OrganizationUnit

    def create(self, validated_data):
        return OrganizationUnit.objects.create(
            **validated_data, organization_business_id=uuid.uuid4()
        )
