from __future__ import unicode_literals

import uuid
from django.db import models

# Create your models here.


class Company(models.Model):
    """
    Model to store company information
    """
    CHAR_LIMIT = 255
    PHONE_LIMIT = 10

    company_name = models.CharField(max_length=CHAR_LIMIT)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos', null=True, blank=True, max_length=CHAR_LIMIT)
    founded_on = models.DateField()
    website = models.URLField(max_length=CHAR_LIMIT)
    linkedin_url = models.URLField(max_length=CHAR_LIMIT)
    twitter_url = models.URLField(max_length=CHAR_LIMIT)
    email = models.EmailField()
    phone_number = models.CharField(max_length=PHONE_LIMIT)
    profile_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)


class FundingDetail(models.Model):
    """
    Model to store funding information
    """
    SERIES_A = 1
    SERIES_B = 2
    SERIES_C = 3
    SERIES_D = 4
    SERIES_E = 5
    SERIES_F = 6

    STAGE_CHOICES = (
        (SERIES_A, 'Series A'),
        (SERIES_B, 'Series B'),
        (SERIES_C, 'Series C'),
        (SERIES_D, 'Series D'),
        (SERIES_E, 'Series E'),
        (SERIES_F, 'Series F'),
    )

    investor = models.ForeignKey(Company, help_text="Company that invested", related_name='investees')
    company = models.ForeignKey(Company, help_text="Company being invested in", related_name='investors')
    amount = models.IntegerField(help_text="Amount invested")
    stage = models.PositiveIntegerField(choices=STAGE_CHOICES, default=SERIES_A)


class Market(models.Model):
    """
    Model to store tag information for a company
    """
    TAG_LIMIT= 255

    company = models.ForeignKey(Company)
    tag = models.CharField(max_length=TAG_LIMIT)
