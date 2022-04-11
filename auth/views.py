# django imports
from django.contrib.auth.models import User
# DRF imports
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
# Elenas imports
from .serializers import SignInSerializer, SingUpSerializer 


class SignInAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = SignInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        
        return Response({
            'token': token
        }, status=status.HTTP_201_CREATED)

# Create your views here.
class SignUpView(generics.CreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = SingUpSerializer