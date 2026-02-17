from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Design, DesignCategory
from .serializers import DesignSerializer, DesignCategorySerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

# Create your views here.
class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)
        if user is not None:
            refresh =RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({
            "error": "You're not NDALUKEE"
        }, status=status.HTTP_400_BAD_REQUEST)



class ListCreateDesignCategoryView(ListCreateAPIView):
    queryset = DesignCategory.objects.all()
    serializer_class = DesignCategorySerializer
    permission_classes = [IsAdminUser]

class UpdateDestroyDesignCategoryView(RetrieveUpdateDestroyAPIView):
    queryset = DesignCategory.objects.all()
    serializer_class = DesignCategorySerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'

class ListCreateDesignView(ListCreateAPIView):
    queryset = Design.objects.all()
    serializer_class = DesignSerializer
    permission_classes = [IsAdminUser]

class UpdateDestroyDesignView(RetrieveUpdateDestroyAPIView):
    queryset = Design.objects.all()
    serializer_class = DesignSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'

