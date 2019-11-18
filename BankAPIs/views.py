from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED
)

from .serializers import BankBranchSerializer
from .models import Bank_Branches


class getBankDetails(APIView):

    bank_branch_serializer_class = BankBranchSerializer
    
    def get(self, request, format = None):

        ifsc = request.query_params.get('ifsc')
        name = request.query_params.get('name')
        city = request.query_params.get('city')

        if ifsc:
            
            branches = Bank_Branches.objects.filter(ifsc=ifsc).all()
            serializer = BankBranchSerializer(branches, many =True)
            return Response(serializer.data)

        elif name and city:

            branches = Bank_Branches.objects.filter(bank_name = name, 
                                                        city=city).all()

        else:
            
            branches = Bank_Branches.objects.all()

        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(branches, request)        
        serializer = BankBranchSerializer(result_page, many = True)

        return Response({
            'links': {
                'next': paginator.get_next_link(),
                'previous': paginator.get_previous_link()
            },
            'count': paginator.count,
            'results': serializer.data
        })



class RegisterUsers(CreateAPIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        
        if not username and not password:
            return Response(
                data={
                    "message": "username, password is required to register a user"
                },
                status=HTTP_400_BAD_REQUEST
            )
        
        new_user = User.objects.create_user(
            username=username, password=password)

        return Response(status=HTTP_201_CREATED)        