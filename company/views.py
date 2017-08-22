from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin

from company import serializers, models
# Create your views here.


class CompanyCreateRetrieveViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    """
    A viewset that provides retrieve and create actions for Company and other related data
    """
    lookup_field = 'profile_id'
    serializer_class = serializers.CompanySerializer
    queryset = models.Company.objects.all()
