from django.conf.urls import url, include
from rest_framework import routers

from company import views

router = routers.DefaultRouter()
router.register(r'company', views.CompanyCreateRetrieveViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
