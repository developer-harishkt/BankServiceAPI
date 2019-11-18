from django.conf.urls import url
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import (
    getBankDetails,
    RegisterUsers
)


urlpatterns = [
    url(r'^getBankDetails/', getBankDetails.as_view(), name = 'getBank'),
    url(r'^token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^refresh/', TokenRefreshView.as_view(), name='token_refresh'),        
    url(r'^token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    url(r'^register/', RegisterUsers.as_view(), name="api-register")
]

