from company import models
from rest_framework import serializers


class FundingSerializer(serializers.ModelSerializer):
    """
    Serializer for Funding Details
    """
    investor = serializers.UUIDField(format='hex_verbose')

    def validate_investor(self, investor_profile_id):
        """
        Method to validate Investor's Profile ID passed
        :param investor_profile_id:
        :return: Investor's profile ID
        """
        if not models.Company.objects.filter(profile_id=investor_profile_id).exists():
            raise serializers.ValidationError("Investor does not exists")
        return investor_profile_id

    class Meta:
        model = models.FundingDetail
        fields = ('investor', 'amount', 'stage')


class MarketSerializer(serializers.ModelSerializer):
    """
    Serializer for Market
    """

    class Meta:
        model = models.Market
        fields = ('tag',)


class CompanySerializer(serializers.ModelSerializer):
    """
    Serializer for Company
    """
    logo = serializers.ImageField(required=False)
    linkedin_url = serializers.CharField(required=False)
    twitter_url = serializers.CharField(required=False)
    profile_id = serializers.UUIDField(read_only=True)
    funding_details = FundingSerializer(required=False, many=True)
    market = serializers.ListField(required=False, child=serializers.CharField(max_length=models.Market.TAG_LIMIT))

    class Meta:
        model = models.Company
        fields = (
            'company_name', 'description', 'logo', 'founded_on',
            'website', 'linkedin_url', 'twitter_url', 'email', 'phone_number', 'profile_id', 'funding_details', 'market')

    def create(self, validated_data):
        funding_details = validated_data.pop('funding_details', None)
        market_data = validated_data.pop('market', [])
        company = models.Company.objects.create(**validated_data)
        if funding_details:
            funding_objects = [
                models.FundingDetail(
                    company=company,
                    investor=models.Company.objects.get(profile_id=fund_data.get('investor')),
                    amount=fund_data.get('amount'),
                    stage=fund_data.get('stage')
                )
                for fund_data in funding_details
            ]
            models.FundingDetail.objects.bulk_create(funding_objects)

        market_objects = [
            models.Market(
                company=company,
                tag=tag
            )
            for tag in market_data
        ]
        models.Market.objects.bulk_create(market_objects)
        return company

    @property
    def data(self):
        data = super(CompanySerializer, self).data
        data['funding_details'] = FundingSerializer(self.instance.investors.all(), many=True).data or []
        data['markets'] = MarketSerializer(self.instance.market_set.all(), many=True).data or []
        return data
