from rest_framework.serializers import ModelSerializer
from .models import Bank_Branches


class BankBranchSerializer(ModelSerializer):

    allow_null = True
    
    class Meta:
        model = Bank_Branches
        fields = "__all__"