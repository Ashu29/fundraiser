from company import models
from rest_framework import serializers


class FundingSerializer(serializers.ModelSerializer):
    """
    Serializer for Funding Details
    """

    class Meta:
        model = models.FundingDetail


class MarketSerializer(serializers.ModelSerializer):
    """
    Serializer for Market
    """

    class Meta:
        model = models.Market


class CompanySerializer(serializers.ModelSerializer):
    """
    Serializer for Company
    """
    logo = serializers.ImageField(required=False)
    linkedin_url = serializers.CharField(required=False)
    twitter_url = serializers.CharField(required=False)
    profile_id = serializers.UUIDField(read_only=True)
    funding_details = FundingSerializer()
    market = MarketSerializer(many=True)

    class Meta:
        model = models.Company
        fields = (
            'company_name', 'description', 'logo', 'founded_on',
            'website', 'linkedin_url', 'twitter_url', 'email', 'phone_number', 'profile_id', 'funding_details', 'market')